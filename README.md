# gpt-code-commenter

Automatically document code by passing it to an LLM (Chat-GPT).

- With a simple prompt, we ask the LLM to annotate the given code, following conventions for that language.

- `NOTE` - this tool still requires manual supervision: If outputting back to the same location, please check the results before committing the changes. By default the tool outputs to stdout OR to a new directory.

## Usage

To comment a single file:

```
pipenv run python via-chat-gpt <path to source code file> [--out-dir <output directory>]
```

To comment files in a directory (is NOT recursive):

```
pipenv run python via-chat-gpt <path to source code directory> [--out-dir <output directory>] [--exclude <file1.py,file2.ts>]
```

note: to write back to the same file(s), simply specify `--out-dir` to point to the same directory.  But then please check the result before committing changes.

## Example

Example documentation generated (published via pdoc to S3): [cornsnake documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/).

### INPUT:

```
import json

def read_from_json_file(path_to_json, encoding='utf-8'):
    with open(path_to_json, encoding=encoding) as f:
        data = json.load(f)
        return data

def write_to_json_file(dict, file_path, encoding='utf-8', indent=2):
    json_object = json.dumps(dict, indent=indent)

    with open(file_path, "w", encoding=encoding) as outfile:
        outfile.write(json_object)
```

### OUTPUT:

```
"""
This Python file contains functions for reading from and writing to a JSON file. The `read_from_json_file` function reads JSON data from a file, and the `write_to_json_file` function writes JSON data to a file.
"""

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

def write_to_json_file(dict, file_path, encoding='utf-8', indent=2):
    """
    Function to write JSON data to a file.

    Args:
    dict (dict): The dictionary containing JSON data to be written.
    file_path (str): The path to the output JSON file.
    encoding (str): The encoding of the file. Default is 'utf-8'.
    indent (int): The number of spaces to indent the JSON data. Default is 2.
    """
    json_object = json.dumps(dict, indent=indent)  # Convert dictionary to JSON string with specified indent

    with open(file_path, "w", encoding=encoding) as outfile:
        outfile.write(json_object)  # Write JSON data to the file
```

## Set up

### [RECOMMENDED] For openai (remote LLM):

```shell
cd via-chat-gpt
```

Unix:

```shell
pip install pipenv
export PYTHONPATH="${PYTHONPATH}:."
pipenv install
```

Windows:

```shell
pip install pipenv
set PYTHONPATH="%PYTHONPATH%";.
pipenv install
```

Set environment variable with your OpenAI key:

```shell
export OPENAI_API_KEY="xxx"
```

Add that to your shell initializing script (`~/.zprofile` or similar)

Load in current terminal:

```shell
source ~/.zprofile
```

### Test OpenAI

(cd via-chat-gpt)

```shell
test-openai.sh
```

or

```shell
pipenv run python via-chat-gpt ../test-resources/util_json.py
```

### For phi2 (local LLM via llama-cpp-python) [UNIX OR Windows] [EASIER TO INSTALL]

- Results are only OK (Chat-GPT has much better results)

- see [via-phi2-the-bloke README](./via-phi2-the-bloke/README.md)

### For phi2 (local LLM via transformers) [UNIX not Windows] [MORE DIFFICULT TO INSTALL]

- TODO fix reponse handling for this version

- see [via-phi2 README](./via-phi2/README.md)
