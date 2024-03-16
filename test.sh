set -e

python via-chat-gpt ./test-resources/util_json.py

python via-chat-gpt ./test-resources/util_json.py --out-dir ./temp/single-file

python via-chat-gpt ./test-resources

python via-chat-gpt ./test-resources --out-dir ./temp/whole-dir

python via-chat-gpt ./test-resources --out-dir ./temp/whole-dir --exclude util_color.py,util_json.py
