from data import read_data, priorities


def main():
    # data = read_data("test.dat")
    data = read_data("input.dat")

    def comb(tup):
        return tup[0].union(tup[1])

    prio_sum = 0
    for pos in range(0, len(data), 3):
        first = comb(data[pos])
        second = comb(data[pos + 1])
        third = comb(data[pos + 2])

        (common,) = first.intersection(second).intersection(third)

        prio_sum += priorities[common]

    print(prio_sum)


if __name__ == "__main__":
    main()
