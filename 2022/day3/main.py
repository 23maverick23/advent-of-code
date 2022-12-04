import os
import string
from itertools import islice

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = "input.txt"
input_file_path = os.path.join(__location__, input_file)

"""
a - z = 1 - 26
A - Z = 27 - 52

"""

alpha_lower = list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)

def get_item_type(rucksack):
    half = len(rucksack) // 2
    compartment_one, compartment_two = rucksack[:half], rucksack[half:]
    item_type = set(compartment_one) & set(compartment_two)
    return ''.join(item_type)  # convert set to string

def get_group_item_type(rucksacks):
    sack_one, sack_two, sack_three = rucksacks
    sack_one_clean = sack_one.rstrip("\n")
    sack_two_clean = sack_two.rstrip("\n")
    sack_three_clean = sack_three.rstrip("\n")
    item_type = set(sack_one_clean) & set(sack_two_clean) & set(sack_three_clean)
    return ''.join(item_type)  # convert set to string

def get_item_type_priority(item_type):
    alpha_full = alpha_lower + alpha_upper
    return alpha_full.index(item_type) + 1

## Part 1 ##

sum_of_priorities = 0

with open (input_file_path) as f:
    for line in f:
        item_type = get_item_type(line)
        priority = get_item_type_priority(item_type)
        sum_of_priorities += priority

print(f"The sum of the priorities is {sum_of_priorities}")

## Part 2 ##

sum_of_badge_priorities = 0

with open (input_file_path) as f:
    while True:
        next_n_lines = list(islice(f, 3))
        if not next_n_lines:
            break

        # process next_n_lines
        # https://stackoverflow.com/a/6335876
        item_type = get_group_item_type(next_n_lines)
        priority = get_item_type_priority(item_type)
        sum_of_badge_priorities += priority

print(f"The sum of the group badge priorities is {sum_of_badge_priorities}")
