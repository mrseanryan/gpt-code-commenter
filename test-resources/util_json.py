import json

def read_from_json_file(path_to_json, encoding='utf-8'):
    with open(path_to_json, encoding=encoding) as f:
        data = json.load(f)
        return data

def write_to_json_file(dict, file_path, encoding='utf-8', indent=2):
    json_object = json.dumps(dict, indent=indent)

    with open(file_path, "w", encoding=encoding) as outfile:
        outfile.write(json_object)
