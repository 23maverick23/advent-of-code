import os
import string

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                             os.path.dirname(__file__)
                                             ))

input_file = "input.txt"
input_file_path = os.path.join(__location__, input_file)

"""

"""


with open(input_file_path) as f:
    for line in f:
        marker_start = 0
        marker_end = 4

        while True:
            packet = {x for x in line[marker_start:marker_end]}
            if len(packet) == 4:
                break
            marker_start += 1
            marker_end += 1

print(f"The number of characters before start-of-packet is {marker_end}")


with open(input_file_path) as f:
    for line in f:
        marker_start = 0
        marker_end = 14

        while True:
            packet = {x for x in line[marker_start:marker_end]}
            if len(packet) == 14:
                break
            marker_start += 1
            marker_end += 1

print(f"The number of characters before start-of-message is {marker_end}")
