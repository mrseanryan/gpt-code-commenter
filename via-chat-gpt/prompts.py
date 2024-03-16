import json
import config

def ANNOTATE_SRC_CODE(src_code):
    return f'''
Annotate this source code with documentation, using the appropriate format for that language.

SOURCE CODE:
```
{src_code}
```

IMPORTANT: Do NOT skip elements (functions or classes), BUT if the element already has a comment then DO skip it.

EXAMPLE OUTPUT:
```json
{{
    "overall_comment": "_QUOTE__QUOTE__QUOTE_Read and write JSON files._QUOTE__QUOTE__QUOTE_",
    "elements": [{{
        "name": "read_from_json_file",
        "comment": "    _QUOTE__QUOTE__QUOTE_Read JSON data from a file.\\nArgs:\\npath_to_json (str): The path to the JSON file.\\nencoding (str): The encoding of the file. Default is 'utf-8'.\\nReturns:\\ndict: The JSON data read from the file.\\n_QUOTE__QUOTE__QUOTE_"
    }},
{{
        "name": "write_to_json_file",
        "comment": "    _QUOTE__QUOTE__QUOTE_Write JSON data to a file.\\nArgs:\\ndict (dict): The dictionary to be written to the file as JSON.\\nfile_path (str): The path to the output JSON file.\\nencoding (str): The encoding of the file. Default is 'utf-8'.\\nindent (int): The number of spaces to use for indentation. Default is 2.\\n_QUOTE__QUOTE__QUOTE_"
    }}
    ]
}}
```

Make sure that comments have correct indentation.
IMPORTANT: Output MUST be valid JSON. Escape \" with _QUOTE_ and \"\"\" with _QUOTE__QUOTE__QUOTE_.
'''

def _pick_longest(parts):
    max_len = -1
    longest = None
    for part in parts:
        if len(part) > max_len:
            longest = part
            max_len = len(part)
    return longest

def _clean_text(text):
    BAD_TEXTS = ['```json', '```']
    for BAD in BAD_TEXTS:
        if BAD in text:
            parts = text.split(BAD)
            text = _pick_longest(parts)
    return text

def parse_response(response):
    response = _clean_text(response)

    return json.loads(response)

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
