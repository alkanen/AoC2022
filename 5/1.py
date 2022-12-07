from data import read_data


def main():
    stacks, moves = read_data("input.dat")

    for move in moves:
        num, src, dst = move
        for i in range(num):
            stacks[dst].append(stacks[src].pop())

    tops = []
    for key in stacks:
        tops.append(stacks[key][-1])

    print("".join(tops))


if __name__ == "__main__":
    main()
