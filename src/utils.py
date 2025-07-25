import json

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_config(path):
    with open(path) as f:
        return json.load(f)
