set -e

pipenv run python via-chat-gpt ../test-resources/util_json.py

pipenv run python via-chat-gpt ../test-resources/util_json.py --out-dir ./temp/single-file

pipenv run python via-chat-gpt ../test-resources/util_robust_delete_has_comments.py --out-dir ./temp/single-file

pipenv run python via-chat-gpt ../test-resources

pipenv run python via-chat-gpt ../test-resources --out-dir ./temp/whole-dir

pipenv run python via-chat-gpt ../test-resources --out-dir ./temp/whole-dir --exclude util_color.py,util_json.py
