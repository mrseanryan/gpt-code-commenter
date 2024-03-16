import os
import shutil

from . import util_os
from . import util_pdf
from . import util_text

def copy_file(from_path, to_path):
    shutil.copyfile(from_path, to_path)

def get_this_script_dir(this_file):
    """
    Call like this: get_this_script_dir(__file__)
    """
    return os.path.dirname(os.path.realpath(this_file))

def _get_long_file_path(path_to_file):
    return u"\\\\?\\" + path_to_file if util_os.is_windows() else path_to_file

def is_empty_directory_only_subdirectories(path_to_file):
    if os.path.isfile(path_to_file):
        return is_empty_file(path_to_file)
    contents = os.listdir(path_to_file)
    for content in contents:
        path_to_sub = os.path.join(path_to_file, content)
        if os.path.isfile(path_to_sub):
            return is_empty_file(path_to_sub)
        if not os.path.isfile(path_to_sub):
            is_empty = is_empty_directory_only_subdirectories(path_to_sub)
            if not is_empty:
                return False
    return True

def is_empty_file(path_to_file):
    if not os.path.isfile(path_to_file):
        return False
    # skip if it is symbolic link
    if os.path.islink(path_to_file):
        return False

    fp_allow_long_path = _get_long_file_path(path_to_file)
    size = os.path.getsize(fp_allow_long_path)
    return size == 0

def read_lines_from_file(filepath, skip_comments=False):
    lines = []
    with open(filepath, encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    if skip_comments:
        lines = _remove_comments(lines)
    return lines

def read_text_from_file(filepath):
    with open(filepath, encoding='utf-8') as file:
        return file.read()

def _remove_comments(lines):
    filtered_lines = []
    for line in lines:
        if not line.startswith('#'):
            filtered_lines.append(line)
    return filtered_lines

def read_text_from_text_or_pdf_file_skipping_comments(filepath):
    if util_pdf.is_pdf(filepath):
        return util_pdf.extract_text_from_pdf(filepath)
    lines = read_lines_from_file(filepath)
    filtered_lines = _remove_comments(lines)
    return util_text.LINE_END.join(filtered_lines)

def write_text_lines_to_file(lines, filepath):
    with open(filepath, encoding='utf-8', mode='w') as file:
        for line in lines:
            file.write(line + util_text.LINE_END)

def write_array_to_file_skipping_empty(PATH_TO_OUTPUT_TEXT_FILE, lines):
    with open(PATH_TO_OUTPUT_TEXT_FILE, 'w') as f:
        for line in lines:
            if line is not None and len(line) > 0:
                f.write(line + '\n')

def write_text_to_file(text, filepath):
    with open(filepath, "w", encoding='utf-8') as f:
        f.write(text)

def get_last_part_of_path(file_path):
    return file_path.split(os.sep)[-1]
