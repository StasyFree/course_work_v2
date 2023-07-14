from utils import read_file, get_filtered_data, get_sorted_data, put_on_mask, get_formatted
import pytest


@pytest.fixture
def get_test_data():
    data = (
        {
            "id": 214024827,
            "state": "CANCELED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {
                "amount": "70946.18",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366"
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {}
    )
    return data


def test_read_file():
    assert isinstance(read_file('operations.json'), list)


def test_get_filtered_data(get_test_data):
    assert len(get_filtered_data(get_test_data)) == 2


def test_get_sorted_data(get_test_data):
    data = get_filtered_data(get_test_data)
    assert get_sorted_data(data) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]


def test_put_on_mask():
    assert put_on_mask('Maestro 1596837868705199') == "Maestro 1596 83** **** 5199"


def test_get_formatted(get_test_data):
    data = get_filtered_data(get_test_data)
    data = get_sorted_data(data)
    assert get_formatted(data) == ['26.08.2019 Перевод организации \nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n', '03.07.2019 Перевод организации \nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD\n']
