from tqdm import tqdm

from data import read_data


def scores(me: str, them: str):
    return {
        # Rock
        "X": {
            # Rock
            "A": 1 + 3,
            # Paper
            "B": 1 + 0,
            # Scissor
            "C": 1 + 6,
        },
        # Paper
        "Y": {
            # Rock
            "A": 2 + 6,
            # Paper
            "B": 2 + 3,
            # Scissor
            "C": 2 + 0,
        },
        # Scissor
        "Z": {
            # Rock
            "A": 3 + 0,
            # Paper
            "B": 3 + 6,
            # Scissor
            "C": 3 + 3,
        },
    }[me][them]


def main():
    # rounds = read_data("test.dat")
    rounds = read_data("input.dat")

    score = 0
    for round in tqdm(rounds):
        score += scores(round[1], round[0])

    print(score)


if __name__ == "__main__":
    main()
