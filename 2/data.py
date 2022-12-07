def read_data(filename):
    rounds = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            round = tuple(line.split())

            rounds.append(round)

    return rounds
