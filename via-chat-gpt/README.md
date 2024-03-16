# Comment Code via Chat-GPT

With a simple prompt, we can ask the LLM to annotate the given code, following conventions for that language.

## Usage

To comment a single file:

```
python via-chat-gpt <path to source code file> [--out-dir <output directory>]
```

To comment files in a directory (is NOT recursive):

```
python via-chat-gpt <path to source code directory> [--out-dir <output directory>]
```

## Example output

```
xxx
```


## Set up

Unix:

```shell
export PYTHONPATH="${PYTHONPATH}:."
```

Windows:

```shell
set PYTHONPATH="%PYTHONPATH%";.
```

Then on both OS's:

```shell
pipenv install
```

Set environment variable with your OpenAI key:

```
export OPENAI_API_KEY="xxx"
```

Add that to your shell initializing script (`~/.zprofile` or similar)

Load in current terminal:

```
source ~/.zprofile
```

## Test

`test.sh`

or

`pipenv run python via-chat-gpt/main.py ./test-resources/util_json.py`
