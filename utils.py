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


def put_on_mask(data):
    new_data = data.split()
    if len(new_data[1]) == 20:
        new_data[1] = 2 * '*' + new_data[1][-4:]
        return ' '.join(new_data)
    else:
        card = new_data[-1]
        new_data[-1] = card[:4] + ' ' + card[4:6] + 2 * '*' + ' ' + 4 * '*' + ' ' + card[-4:]
        return ' '.join(new_data)


def get_formatted(data):
    operations = []
    for item in data:
        recipient = put_on_mask(item['to'])
        item['date'] = datetime.datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S.%f")
        date = datetime.datetime.strftime(item['date'], "%d.%m.%Y")
        amount = item["operationAmount"]["amount"]
        currency = item["operationAmount"]["currency"]["name"]
        description = item['description']
        if 'from' in item.keys():
            destination = put_on_mask(item['from'])
            operation = f"{date} {description} \n{destination} -> {recipient}\n{amount} {currency}\n"
            operations.append(operation)
        else:
            operation = f"{date} {description} \n -> {recipient}\n{amount} {currency}\n"
            operations.append(operation)
    return operations
