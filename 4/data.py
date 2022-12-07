def read_data(filename):
    areas = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            pairs = [[int(y) for y in x.split("-")] for x in line.split(",")]

            areas.append(pairs)

    return areas
