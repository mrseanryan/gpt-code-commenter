# gpt-code-commenter

Automatically document code by passing it to an LLM (Chat-GPT).

- With a simple prompt, we ask the LLM to annotate the given code, following conventions for that language.

- `NOTE` - this tool still requires manual supervision: currently larger files may become truncated by the LLM.  By default the tool outputs to stdout OR to a new directory.

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

### For openai (remote LLM):

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

```shell
cd via-chat-gpt
test-openai.sh
```

or

```shell
cd via-chat-gpt
pipenv run python via-chat-gpt ../test-resources/util_json.py
```

### For phi2 (local LLM) [MORE DIFFICULT TO INSTALL]

```shell
cd via-phi2
```

At time of writing, phi2 depends on a dev build of transformers, so it can be tricky to install.

See the (model card)[https://huggingface.co/microsoft/phi-2] for details.

```shell
python -m pipenv run pip install transformers==4.38.2
```

OR if that does not work, try the latest dev version:

```shell
python -m pipenv run pip install git+https://github.com/huggingface/transformers
```

```shell
python -m pipenv run pip install cornsnake==0.0.46 packaging==24.0
```

#### WITHOUT GPU:

Install torch (without CUDA) - please check the [PyTorch site](https://pytorch.org/get-started/locally/#windows-pip) for your system.

```shell
python -m pipenv run pip install torch==2.2.1 torchvision==0.17.1
```

Edit `config.py` and set is_gpu to False.

#### WITH GPU:

Install CUDA to match your NVIDIA GPU - see [NVIDIA site](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html).

Install torch (with CUDA) - please check the [PyTorch site](https://pytorch.org/get-started/locally/#windows-pip) for your system.

- example installing torch with CUDA v12.1:

```shell
python -m pipenv run pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

Install ninja, to speed up compile of flash-attn:

```shell
python -m pipenv run pip install ninja
ninja --version
```

Install flash-atten:

```shell
python -m pipenv run pip install flash-attn --no-build-isolation
```

Edit `config.py` and set is_gpu to True.

### Test phi2

```shell
cd via-phi2
test-phi2.sh
```

or

```shell
cd via-phi2
pipenv run python via-phi2 ../test-resources/util_json.py
```
