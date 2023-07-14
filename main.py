from utils import read_file, get_filtered_data, get_sorted_data, get_formatted


def main():
    file = 'operations.json'
    data = read_file(file)
    data = get_filtered_data(data)
    data = get_sorted_data(data)
    data = get_formatted(data)
    for item in data:
        print(item)


if __name__ == '__main__':
    main()
