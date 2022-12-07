from data import read_data, priorities


def main():
    # data = read_data("test.dat")
    data = read_data("input.dat")

    prio_sum = 0
    for sack in data:
        (common,) = sack[0].intersection(sack[1])
        prio_sum += priorities[common]

    print(prio_sum)


if __name__ == "__main__":
    main()
