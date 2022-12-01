from data import read_data


# Overkill, a simple data.sort(reverse=True), sum(data[0:3]) would work :)
def add_count(three_best, new_count):
    for i in range(3):
        if new_count > three_best[i]:
            # print(f"{new_count} larger than {three_best[i]} at {i}")
            for j in range(2, i, -1):
                # print(f"Moving {three_best[j-1]} from {j-1} to {j}")
                three_best[j] = three_best[j - 1]

            three_best[i] = new_count
            break


def main():
    # data = read_data("test.dat")
    data = read_data("input.dat")
    three_best = [0, 0, 0]

    for i, elf in enumerate(data):
        data[i] = sum(elf)
        add_count(three_best, data[i])

    data.sort(reverse=True)
    print(sum(three_best))


if __name__ == "__main__":
    main()
