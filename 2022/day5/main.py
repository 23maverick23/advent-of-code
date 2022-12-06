import os
import string

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = "input.txt"
input_file_path = os.path.join(__location__, input_file)

"""
                [M]     [V]     [L]
[G]             [V] [C] [G]     [D]
[J]             [Q] [W] [Z] [C] [J]
[W]         [W] [G] [V] [D] [G] [C]
[R]     [G] [N] [B] [D] [C] [M] [W]
[F] [M] [H] [C] [S] [T] [N] [N] [N]
[T] [W] [N] [R] [F] [R] [B] [J] [P]
[Z] [G] [J] [J] [W] [S] [H] [S] [G]
 1   2   3   4   5   6   7   8   9

"""

stack_1 = ['Z', 'T', 'F', 'R', 'W', 'J', 'G']
stack_2 = ['G', 'W', 'M']
stack_3 = ['J', 'N', 'H', 'G']
stack_4 = ['J', 'R', 'C', 'N', 'W']
stack_5 = ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M']
stack_6 = ['S', 'R', 'T', 'D', 'V', 'W', 'C']
stack_7 = ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V']
stack_8 = ['S', 'J', 'N', 'M', 'G', 'C']
stack_9 = ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']

class CargoStack:
    def __init__(self, crates, from_stack, to_stack):
        self.crates = crates
        self.from_stack = from_stack
        self.to_stack = to_stack

def process_line(line):
    # https://www.askpython.com/python/string/extract-digits-from-python-string
    nums = [int(x) for x in line.split() if x.isdigit()]
    return CargoStack(nums[0], nums[1], nums[2])

# Part 1

cargo = {
    1: stack_1.copy(),
    2: stack_2.copy(),
    3: stack_3.copy(),
    4: stack_4.copy(),
    5: stack_5.copy(),
    6: stack_6.copy(),
    7: stack_7.copy(),
    8: stack_8.copy(),
    9: stack_9.copy()
}

def move_crates(total_crates, from_stack, to_stack):
    for x in range(total_crates):
        crate = cargo[from_stack].pop()
        cargo[to_stack].append(crate)

with open (input_file_path) as f:
    for line in f:
        instructions = process_line(line)
        move_crates(instructions.crates, instructions.from_stack, instructions.to_stack)

final_cargo_stacks = dict(sorted(cargo.items()))
top_of_stack = [final_cargo_stacks.get(k)[-1] for k in final_cargo_stacks.keys()]

print(f"The final stack arrangement is {''.join(str(e) for e in top_of_stack)}")

# Part 2

cargo = {
    1: stack_1.copy(),
    2: stack_2.copy(),
    3: stack_3.copy(),
    4: stack_4.copy(),
    5: stack_5.copy(),
    6: stack_6.copy(),
    7: stack_7.copy(),
    8: stack_8.copy(),
    9: stack_9.copy()
}

def move_crates_improved(total_crates, from_stack, to_stack):
    to_stack_len = len(cargo[to_stack])
    for x in range(total_crates):
        crate = cargo[from_stack].pop()
        cargo[to_stack].insert(to_stack_len, crate)

with open (input_file_path) as f:
    for line in f:
        instructions = process_line(line)
        move_crates_improved(instructions.crates, instructions.from_stack, instructions.to_stack)

final_cargo_stacks = dict(sorted(cargo.items()))
top_of_stack = [final_cargo_stacks.get(k)[-1] for k in final_cargo_stacks.keys()]

print(f"The final stack rearrangement is {''.join(str(e) for e in top_of_stack)}")
