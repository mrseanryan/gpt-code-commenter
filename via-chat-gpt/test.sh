set -e

python via-chat-gpt ./test-resources/util_json.py

python via-chat-gpt ./test-resources/util_json.py --outdir ./temp/single-file

python via-chat-gpt ./test-resources

python via-chat-gpt ./test-resources --outdir ./temp/whole-dir
