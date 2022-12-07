from data import read_data


def main():
    # data = read_data("test.dat")
    data = read_data("input.dat")

    count = 0
    for pair in data:
        first = set(range(pair[0][0], pair[0][1] + 1))
        second = set(range(pair[1][0], pair[1][1] + 1))

        # print(first)
        # print(second)
        if first.issubset(second) or second.issubset(first):
            # print("  yes")
            count += 1
        # print("")

    print(count)


if __name__ == "__main__":
    main()
