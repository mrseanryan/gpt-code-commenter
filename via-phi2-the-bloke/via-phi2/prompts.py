import json
import config

from cornsnake import util_print

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

The output MUST be as *valid* JSON only.
'''

def _clean_text(text):
    BAD_TEXTS_BEFORE = ['```json']
    for BAD in BAD_TEXTS_BEFORE:
        if BAD in text:
            parts = text.split(BAD)
            text = parts[1]
    BAD_TEXTS_AFTER = ['```', '"""']
    for BAD in BAD_TEXTS_AFTER:
        if BAD in text:
            parts = text.split(BAD)
            text = parts[0]
    last_ending_brace = text.rfind('}')
    return text[:last_ending_brace + 1]

def parse_response(response):
    try:
        response = _clean_text(response)

        return json.loads(response)
    except Exception:
        util_print.print_error(f"Could not parse to JSON: {response}")
        raise

def dummy_response():
    if not config.is_dry_run:
        return None

    return '''
```json
{{
    "overall_comment": "Read and write JSON files.",
    "elements": [{{
        "definition": "def read_from_json_file(path_to_json, encoding='utf-8'):",
        "comment": "    Read JSON data from a file.\\nArgs:\\npath_to_json (str): The path to the JSON file.\\nencoding (str): The encoding of the file. Default is 'utf-8'.\\nReturns:\\ndict: The JSON data read from the file.\\n"
    }}
    ]
}}
```
blah
blah
blah
'''
