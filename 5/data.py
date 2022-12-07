from collections import defaultdict, deque


def read_data(filename):
    stacks = defaultdict(deque)
    moves = []

    in_stacks = True

    with open(filename) as f:
        for line in f:
            line = line[:-1]

            if not line:
                in_stacks = False
                for key in stacks:
                    # Remove stack numbers
                    stacks[key].popleft()

                    # Remove empty tops
                    while stacks[key][-1] is None:
                        stacks[key].pop()

            if in_stacks:
                crates = [line[idx : idx + 4].strip() for idx in range(0, len(line), 4)]
                for i, crate in enumerate(crates):
                    stacks[i + 1].appendleft(
                        (crate[1] if crate[0] == "[" else crate) if crate else None
                    )

            else:
                if not line:
                    continue
                instruction = line.split()

                moves.append(
                    (int(instruction[1]), int(instruction[3]), int(instruction[5]))
                )

    return (stacks, moves)
