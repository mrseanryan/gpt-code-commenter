import os

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
    util_file.write_text_to_file(result, out_file_path)

def comment_file(path_to_src_file, options):
    util_print.print_section(f"Reading code from {[path_to_src_file]}")
    code = util_file.read_text_from_file(path_to_src_file)
    response = service_chat.send_prompt(prompts.ANNOTATE_SRC_CODE(code), dummy_response=prompts.dummy_response())
    (overall_comment, commented_code) = prompts.parse_response(response)

    if options.out_dir is None:
        util_print.print_custom(overall_comment)
        util_print.print_custom(commented_code)
    else:
        text = overall_comment + commented_code
        util_dir.ensure_dir_exists(options.out_dir)
        _write_new_code(text, os.path.basename(path_to_src_file), options.out_dir)
