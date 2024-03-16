import json

import config

def ANNOTATE_SRC_CODE(src_code):
    return f'''
Annotate this source code with documentation, using the appropriate format for that language:

```
{src_code}
```
'''

def _clean_text(text):
    lines = text.split('\n')
    clean_lines = []
    for line in lines:
        is_clean = True
        BAD_TEXTS = ['```json', '```']
        for BAD in BAD_TEXTS:
            if BAD in line:
                is_clean = False
                break
        if is_clean:
            clean_lines.append(line)
    return '\n'.join(clean_lines)


def parse_response(response):
    return _clean_text(response)


def dummy_response():
    if not config.is_dry_run:
        return None

    return '''
```
# File: colors.py
# Description: Contains color-related functionality including ANSI escape codes for text color formatting.
# Author: [Author Name]

from . import config

class bcolors:
    """Class containing ANSI escape codes for text color formatting."""
    HEADER = '\033[95m'
    DARK_BLUE = '\033[34m'
    DARK_MAGENTA = '\033[35m'
    DARK_CYAN = '\033[36m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorize(text, color):
    """
    Colorize the given text with the specified color.

    Args:
        text (str): The text to be colorized.
        color (str): The ANSI escape code for the desired color.

    Returns:
        str: The colorized text.
    """
    start_color = color if config.IS_COLOR_ENABLED else ""
    end_color = bcolors.ENDC if config.IS_COLOR_ENABLED else ""
    colorized = f"{start_color}{text}{end_color}"
    return colorized

# Theming
CONFIG_COLOR = bcolors.DARK_MAGENTA
"""Color for configuration information."""

IMPORTANT = bcolors.WARNING
"""Color for important messages."""

QUESTION_COLOR = bcolors.DARK_CYAN
"""Color for questions."""

RESULT_COLOR = bcolors.OKGREEN + bcolors.BOLD
"""Color for results."""

SECTION_COLOR = bcolors.OKBLUE + bcolors.BOLD
"""Color for section headings."""

TEST_SECTION_COLOR = bcolors.WARNING + bcolors.BOLD
"""Color for test sections."""

ERROR_COLOR = bcolors.FAIL + bcolors.BOLD
"""Color for error messages."""

WARNING_COLOR = bcolors.WARNING + bcolors.BOLD
"""Color for warning messages."""

END_COLORS = bcolors.ENDC
"""End color code."""
```
'''
