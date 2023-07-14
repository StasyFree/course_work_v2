import json


def read_file(file):
    with open(file, encoding='utf-8') as f:
        new_file = json.load(f)
    return new_file

