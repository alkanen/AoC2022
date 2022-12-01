import json

from data import read_data


def main():
    # data = read_data("test.dat")
    data = read_data("input.dat")

    for i, elf in enumerate(data):
        data[i] = sum(elf)

    print(max(data))


if __name__ == "__main__":
    main()
