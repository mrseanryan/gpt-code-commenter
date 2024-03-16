import os

from cornsnake import util_file, util_wait, util_print, util_dir

import prompts
import service_chat

def percent(num, denom, ndigits = 0):
    if denom == 0:
        return format(0, f'.{ndigits}f')
    return str(round((num * 100.0) / denom, ndigits)) + '%'

def comment_directory(path_to_src_dir, out_dir):
    files = util_dir.find_files(path_to_src_dir)
    for file in files:
        comment_file(file, out_dir)
        util_wait.wait_seconds(1)
    util_print.print_result(f"Processed {len(files)} files")

def _write_new_code(result, file_name, out_dir):
    out_file_path = os.path.join(out_dir, file_name)
    util_print.print_section(f"Saving commented code to {out_file_path}")
    util_file.write_text_to_file(result, out_file_path)

def comment_file(path_to_src_file, out_dir):
    util_print.print_section(f"Reading code from {[path_to_src_file]}")
    code = util_file.read_text_from_file(path_to_src_file)
    response = service_chat.send_prompt(prompts.ANNOTATE_SRC_CODE(code), dummy_response=prompts.dummy_response())
    result = prompts.parse_response(response)

    if out_dir is None:
        util_print.print_custom(result)
    else:
        _write_new_code(result, os.path.basename(path_to_src_file), out_dir)
