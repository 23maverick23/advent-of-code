import os
import heapq

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = "input.txt"
output_list = []

with open (os.path.join(__location__, input_file)) as f:
    temp_val = 0
    for line in f:
        # print(line, end='')  # DEBUG
        if line in ['\n', '\r\n']:
            output_list.append(temp_val)
            temp_val = 0
        else:
            temp_val += int(line)

print(f"The elf with the most calories has {max(output_list)} calories")
print(f"The three elves with the most calories have {sum(heapq.nlargest(3, output_list))} calories")
