import json
import datetime


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


def get_sorted_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def mask(data):
    new_data = data.split()
    if len(new_data[1]) == 20:
        new_data[1] = 2 * '*' + new_data[1][-4:]
        return ' '.join(new_data)
    else:
        card = new_data[-1]
        new_data[-1] = card[:4] + ' ' + card[4:6] + 2 * '*' + ' ' + 4 * '*' + ' ' + card[-4:]
        return ' '.join(new_data)



