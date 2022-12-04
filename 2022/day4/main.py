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

def full_range(start, end):
    '''range is not inclusive of end, so create new func wrapper'''
    return range(start, end+1)

assignment_contains = 0
assignment_overlaps = 0

with open (input_file_path) as f:
    for line in f:
        assign_one, assign_two = line.rstrip("\n").split(",")

        assign_one_start, assign_one_stop = assign_one.split("-")
        assign_two_start, assign_two_stop = assign_two.split("-")

        assign_one_range = full_range(int(assign_one_start), int(assign_one_stop))
        assign_two_range = full_range(int(assign_two_start), int(assign_two_stop))

        check_one = all(section in list(assign_one_range) for section in list(assign_two_range))
        check_two = all(section in list(assign_two_range) for section in list(assign_one_range))

        check_three = any(section in list(assign_one_range) for section in list(assign_two_range))
        check_four = any(section in list(assign_one_range) for section in list(assign_two_range))

        ## Part 1 ##
        if check_one or check_two:
            assignment_contains += 1

        ## Part 2 ##
        if check_three or check_four:
            assignment_overlaps += 1

print(f"The number of containing assignment pairs is {assignment_contains}")
print(f"The number of overlapping assignment pairs is {assignment_overlaps}")
