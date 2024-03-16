import os
import sys

from cornsnake import util_print

import main

def _print_usage_and_exit():
    print(f"USAGE: {sys.argv[0]} <path to source code file OR directory> [--out-dir <output directory>] [--exclude <file1.py,file2.ts>]")
    exit(42)

class Options:
    def __init__(self):
        out_dir = None
        exclude = None
    def try_parse_options(self, option, value):
        if option == "--out-dir":
            self.out_dir = value
        elif option == "--exclude":
            self.exclude = [v.strip() for v in value.split(',')]

if __name__ == '__main__':
    len_args = len(sys.argv)
    path_to_src_file_or_dir = None
    out_dir = None
    try:
        options = Options()
        if len_args == 2:
            path_to_src_file_or_dir = sys.argv[1]
        elif len_args == 4:
            path_to_src_file_or_dir = sys.argv[1]
            options.try_parse_options(sys.argv[2], sys.argv[3])
        elif len_args == 6:
            path_to_src_file_or_dir = sys.argv[1]
            options.try_parse_options(sys.argv[2], sys.argv[3])
            options.try_parse_options(sys.argv[4], sys.argv[5])
        else:
            raise ValueError(f"Invalid args")
    except:
        _print_usage_and_exit()

    if not os.path.exists(path_to_src_file_or_dir):
        util_print.print_error(f"No such file or directory: {path_to_src_file_or_dir}")
        sys.exit(43)
    if os.path.isdir(path_to_src_file_or_dir):
        main.comment_directory(path_to_src_file_or_dir, options)
    else:
        main.comment_file(path_to_src_file_or_dir, options)
