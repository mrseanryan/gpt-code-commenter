import json
import config

def ANNOTATE_SRC_CODE(src_code):
    return f'''
Provide comments in JSON format for the classes and functions of this source code.

SOURCE CODE:
```
{src_code}
```

OUTPUT FORMAT:
```json
{{
    "overall_comment": <overall comment>,
    "elements": [{{
        "name": <class or function name>,
        "comment": <comment>
    }}
    ]
}}
```
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
