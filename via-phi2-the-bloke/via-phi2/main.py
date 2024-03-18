import os
import traceback

from cornsnake import util_file, util_wait, util_print, util_dir

import prompts
import service_chat

def percent(num, denom, ndigits = 0):
    if denom == 0:
        return format(0, f'.{ndigits}f')
    return str(round((num * 100.0) / denom, ndigits)) + '%'

def comment_directory(path_to_src_dir, options):
    files = util_dir.find_files(path_to_src_dir)
    files_processed = 0
    files_skipped = 0
    for file in files:
        if options.exclude and os.path.basename(file) in options.exclude:
            util_print.print_custom(f"Skippping file {file}")
            files_skipped += 1
            continue
        comment_file(file, options)
        files_processed += 1
        util_wait.wait_seconds(1)
    util_print.print_result(f"Processed {files_processed} files - skipped {files_skipped} files.")

def _write_new_code(result, file_name, out_dir):
    out_file_path = os.path.join(out_dir, file_name)
    util_print.print_section(f"Saving commented code to {out_file_path}")
    result += '\n'
    util_file.write_text_to_file(result, out_file_path)

def _insert_comments(text, elements, extension):
    lines = text.split('\n')
    for element in elements:
        if 'comment' not in element or not element['comment']:
            continue
        line_num = -1
        found = False
        for line in lines:
            line_num += 1
            if element['name'] in line:
                lines[line_num] = line + '\n' + _format_as_comment(_unquote(element['comment']), extension)
                found = True
                break
        if not found:
            util_print.print_warning(f"Could not match AI element '{element['name']}' to a line of the file")
    return '\n'.join(lines)

def _unquote(text):
    return text.replace("_QUOTE_", '"')

def _is_comment_line(line):
    line = line.strip()
    comment_chars = ['"""', '#', '/*', '//', '--']
    for comment_char in comment_chars:
        if line.startswith(comment_char):
            return True
    return False

# Small LLM is not smart enough for a prompt that asks for comment suitable for that programming language.
# (trying to ask for that, affects the valid JSON output)
def _format_as_comment(text, extension, is_overall=False):
    if extension == '.py':
        indent = '' if is_overall else '    '
        return f'{indent}"""\n{text}\n"""'
    if extension == '.sql':
        return f'/*\n{text}\n*/'
    if extension in ['.ts', '.js', '.cs', '.c', '.cpp', '.java']:
        return f'/*\n{text}\n*/'
    raise ValueError(f"Not a recognised file extension: {extension}")

def comment_file(path_to_src_file, options):
    util_print.print_section(f"Reading code from {[path_to_src_file]}")
    code = util_file.read_text_from_file(path_to_src_file)

    (_file_name, extension) = os.path.splitext(path_to_src_file.lower())

    retries = 3
    # This small llm (phi2) only sometimes generates valid JSON
    #
    # TODO - try grammars - https://til.simonwillison.net/llms/llama-cpp-python-grammars
    while(retries > 0):
        try:
            response = service_chat.send_prompt(prompts.ANNOTATE_SRC_CODE(code), dummy_response=prompts.dummy_response())
            comments = prompts.parse_response(response)

            if options.out_dir is None:
                util_print.print_custom(comments)
            else:
                text = ""
                # only add the overall file comment, if the file does not already have a comment
                if _is_comment_line(code):
                    text = code
                else:
                    if 'overall_comment' in comments:
                        text = _format_as_comment(_unquote(comments['overall_comment']), extension, is_overall=True) + '\n' + code
                text = _insert_comments(text, comments['elements'], extension)
                util_dir.ensure_dir_exists(options.out_dir)
                _write_new_code(text, os.path.basename(path_to_src_file), options.out_dir)
            retries = 0
        except Exception as e:
            util_print.print_error(e)
            traceback.print_exc()
            util_print.print_custom("Retrying...")
            retries -= 1
