import config

def ANNOTATE_SRC_CODE(src_code):
    return f'''
Annotate this source code with documentation, using the appropriate format for that language.
At the top of the file, add a comment on the overall file.

SOURCE CODE:
```
{src_code}
```

IMPORTANT: Output using the following format:

```overall
<overall comment>
```

```code
<commented code>
```

IMPORTANT: Do NOT skip lines or functions.
You MUST output the entire file.

EXAMPLE OUTPUT:
```overall
"""
Functions for reading from a JSON file. The `read_from_json_file` function reads JSON data from a file.
"""
```

```code
import json

def read_from_json_file(path_to_json, encoding='utf-8'):
    """
    Function to read JSON data from a file.

    Args:
    path_to_json (str): The path to the JSON file.
    encoding (str): The encoding of the file. Default is 'utf-8'.

    Returns:
    dict: The JSON data read from the file.
    """
    with open(path_to_json, encoding=encoding) as f:
        data = json.load(f)  # Load JSON data from the file
        return data
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
    OVERALL_COMMENT_TOKEN = "```overall"
    COMMENTED_CODE_TOKEN = "```code"

    file_parts = response.split(COMMENTED_CODE_TOKEN)
    overall_comment = file_parts[0].split(OVERALL_COMMENT_TOKEN)[1]

    code = file_parts[1]

    return (_clean_text(overall_comment), _clean_text(code))

def dummy_response():
    if not config.is_dry_run:
        return None

    return '''
```overall
"""
This Python file defines color constants and a function for colorizing text based on the color constants.
"""
```

```code
from . import config

class bcolors:
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
    Function to colorize text based on the provided color.

    Args:
    text (str): The text to be colorized.
    color (str): The color to apply to the text.

    Returns:
    str: The colorized text.
    """
    start_color = color if config.IS_COLOR_ENABLED else ""
    end_color = bcolors.ENDC if config.IS_COLOR_ENABLED else ""
    colorized = f"{start_color}{text}{end_color}"
    return colorized

# Theming
CONFIG_COLOR = bcolors.DARK_MAGENTA
IMPORTANT = bcolors.WARNING
QUESTION_COLOR = bcolors.DARK_CYAN
RESULT_COLOR = bcolors.OKGREEN + bcolors.BOLD
SECTION_COLOR = bcolors.OKBLUE + bcolors.BOLD
TEST_SECTION_COLOR = bcolors.WARNING + bcolors.BOLD
ERROR_COLOR = bcolors.FAIL + bcolors.BOLD
WARNING_COLOR = bcolors.WARNING + bcolors.BOLD
END_COLORS = bcolors.ENDC
```
'''
