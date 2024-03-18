set -e

python -m pipenv run via-chat-gpt ../test-resources/util_json.py

python -m pipenv run via-chat-gpt ../test-resources/util_json.py --out-dir ./temp/single-file

python -m pipenv run via-chat-gpt ../test-resources/util_robust_delete_has_comments.py --out-dir ./temp/single-file

python -m pipenv run via-chat-gpt ../test-resources

python -m pipenv run via-chat-gpt ../test-resources --out-dir ./temp/whole-dir

python -m pipenv run via-chat-gpt ../test-resources --out-dir ./temp/whole-dir --exclude util_color.py,util_json.py
