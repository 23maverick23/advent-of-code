from input import data

def part_one(data):
    total = 0
    prev = 0

    for num in data:
        num = int(num)
        if prev and prev == num:
            total += num
        prev = num

    if int(data[0]) == int(data[-1]):
        total += int(data[0])

    return total

print('\nThe solution to part one of the captcha is \033[1m\033[93m{}\033[0m.\n'.format(part_one(data)))


def part_two(data):
    total = 0
    length = int(len(data))
    mid = int(length/2)

    for num in data:
        num = int(num)
        if num == int(data[mid]):
            total += num

        mid += 1
        if mid >= length:
            mid -= length

    return total

print('\nThe solution to part two of the captcha is \033[1m\033[93m{}\033[0m.\n'.format(part_two(data)))
