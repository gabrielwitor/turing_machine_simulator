import json

def parse_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path {path} does not exist.")