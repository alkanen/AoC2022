def read_data(filename):
    elves = []
    with open(filename) as f:
        calories = []
        for line in f:
            line = line.strip()
            if not line:
                elves.append(calories)
                calories = []
                continue

            calories.append(int(line))

        if calories:
            elves.append(calories)

    return elves
