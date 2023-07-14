from utils import read_file, get_filtered_data


def test_read_file():
    assert isinstance(read_file('operations.json'), list)

