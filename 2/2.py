from tqdm import tqdm

from data import read_data


def scores(me, them):
    return {
        # Lose
        "X": {
            # Rock, pick scissor
            "A": 3 + 0,
            # Paper, pick rock
            "B": 1 + 0,
            # Scissor, pick paper
            "C": 2 + 0,
        },
        # Draw
        "Y": {
            # Rock, pick rock
            "A": 1 + 3,
            # Paper, pick paper
            "B": 2 + 3,
            # Scissor, pick scissor
            "C": 3 + 3,
        },
        # Win
        "Z": {
            # Rock, pick paper
            "A": 2 + 6,
            # Paper, pick scissor
            "B": 3 + 6,
            # Scissor, pick rock
            "C": 1 + 6,
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
