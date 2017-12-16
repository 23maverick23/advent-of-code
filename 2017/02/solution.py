from input import data


def part_one(data):
    total = 0

    for row in data:
        row_min = min(row)
        row_max = max(row)
        total += abs(row_max-row_min)

    return total

print('\nThe solution to part one of the checksum is \033[1m\033[93m{}\033[0m.\n'.format(part_one(data)))


import itertools

def part_two(data):
    total = 0

    for row in data:
        sorted_row = sorted(row, reverse=True)
        for a, b in itertools.combinations(sorted_row, 2):
            a, b = int(a), int(b)
            if a % b == 0:
                total += int(a/b)

    return total

print('\nThe solution to part two of the checksum is \033[1m\033[93m{}\033[0m.\n'.format(part_two(data)))
