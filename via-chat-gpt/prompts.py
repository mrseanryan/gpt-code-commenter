import json
import config

def ANNOTATE_SRC_CODE(src_code):
    return f'''
Comment the element definitions (classes and functions) of this source code with documentation, using the appropriate format for that language.

SOURCE CODE:
```
{src_code}
```

If the element already has a comment then do NOT output for that element.


EXAMPLE INPUT:
```
import json

def read_from_json_file(path_to_json, encoding='utf-8'):
    with open(path_to_json, encoding=encoding) as f:
        data = json.load(f)
        return data
```

EXAMPLE OUTPUT:
```json
{{
    "overall_comment": "_QUOTE__QUOTE__QUOTE_Read and write JSON files._QUOTE__QUOTE__QUOTE_",
    "elements": [{{
        "definition": "def read_from_json_file(path_to_json, encoding='utf-8'):",
        "comment": "    _QUOTE__QUOTE__QUOTE_Read JSON data from a file.\\nArgs:\\npath_to_json (str): The path to the JSON file.\\nencoding (str): The encoding of the file. Default is 'utf-8'.\\nReturns:\\ndict: The JSON data read from the file.\\n_QUOTE__QUOTE__QUOTE_"
    }}
    ]
}}
```

IMPORTANT:
- Make sure that comments have correct indentation.
- Do NOT comment on elements that already have a comment.
- Output MUST be valid JSON. Escape \" with _QUOTE_ and \"\"\" with _QUOTE__QUOTE__QUOTE_.
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
```json
{{
    "overall_comment": "_QUOTE__QUOTE__QUOTE_Read and write JSON files._QUOTE__QUOTE__QUOTE_",
    "elements": [{{
        "definition": "def read_from_json_file(path_to_json, encoding='utf-8'):",
        "comment": "    _QUOTE__QUOTE__QUOTE_Read JSON data from a file.\\nArgs:\\npath_to_json (str): The path to the JSON file.\\nencoding (str): The encoding of the file. Default is 'utf-8'.\\nReturns:\\ndict: The JSON data read from the file.\\n_QUOTE__QUOTE__QUOTE_"
    }}
    ]
}}
```
'''
