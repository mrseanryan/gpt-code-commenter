import os
import sys

from cornsnake import util_print

import main

def _print_usage_and_exit():
    print(f"USAGE: {sys.argv[0]} <path to source code file OR directory> [--out-dir <output directory>]")
    exit(42)

if __name__ == '__main__':
    len_args = len(sys.argv)
    path_to_src_file_or_dir = None
    out_dir = None
    if len_args == 2:
        path_to_src_file_or_dir = sys.argv[1]
    elif len_args == 4:
        path_to_src_file_or_dir = sys.argv[1]
        if sys.argv[2] == '--out-dir':
            out_dir = sys.argv[3]
        else:
            _print_usage_and_exit()
    else:
        _print_usage_and_exit()

    if not os.path.exists(path_to_src_file_or_dir):
        util_print.print_error(f"No such file or directory: {path_to_src_file_or_dir}")
        sys.exit(43)
    if os.path.isdir(path_to_src_file_or_dir):
        main.comment_directory(path_to_src_file_or_dir, out_dir)
    else:
        main.comment_file(path_to_src_file_or_dir, out_dir)
