import json


def read_file(file):
    with open(file, encoding='utf-8') as f:
        new_file = json.load(f)
    return new_file


def get_filtered_data(data):
    new_data = []
    for item in data:
        if 'state' in item.keys():
            if item["state"] == 'EXECUTED':
                new_data.append(item)
    return new_data
