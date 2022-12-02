import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = "input.txt"
output_list = []

"""
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors

1 for Rock, 2 for Paper, and 3 for Scissors
0 if you lost, 3 if the round was a draw, and 6 if you won

A Y -> 2+6=8
B X -> 1+0=1
C Z -> 3+3=6

"""
running_points_total = 0
running_points_total2 = 0

CHOICE_POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

OUTCOME_POINTS = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

OUTCOME_TEXT = {
    0: "lost",
    3: "tied",
    6: "won"
}

def get_choice_points(val):
    return CHOICE_POINTS[val]

def get_outcome_points(first, second):
    concat = first + second

    # handle ties
    if concat in ("AX", "BY", "CZ"):
        return 3

    # handle losses
    if concat in ("AZ", "BX", "CY"):
        return 0

    # handle wins
    if concat in ("AY", "BZ", "CX"):
        return 6

def get_outcome_choice(first, result):
    if result == "X":
        value_losses = {"A": "Z", "B": "X", "C": "Y"}
        return value_losses[first]

    if result == "Y":
        value_ties = {"A": "X", "B": "Y", "C": "Z"}
        return value_ties[first]

    if result == "Z":
        value_wins = {"A": "Y", "B": "Z", "C": "X"}
        return value_wins[first]

def get_round_points(opponent, myself):
    my_points = CHOICE_POINTS[myself]
    outcome_points = get_outcome_points(opponent, myself)
    round_points = my_points + outcome_points
    # print(f"{round_points}: {my_points} for choosing {myself}, and {outcome_points} because you {OUTCOME_TEXT[outcome_points]}")
    return round_points

def get_round_points2(opponent, result):
    my_choice = get_outcome_choice(opponent, result)  # returns string
    my_points = CHOICE_POINTS[my_choice]
    outcome_points = OUTCOME_POINTS[result]
    round_points = my_points + outcome_points
    return round_points

with open (os.path.join(__location__, input_file)) as f:
    for line in f:
        choices = [*line.replace(" ", "").rstrip("\n")]
        running_points_total += get_round_points(choices[0], choices[1])

print(f"The total score for following the strategy guide is {running_points_total}")

with open (os.path.join(__location__, input_file)) as f:
    for line in f:
        choices = [*line.replace(" ", "").rstrip("\n")]
        running_points_total2 += get_round_points2(choices[0], choices[1])

print(f"The total score for following the updated strategy guide is {running_points_total2}")
