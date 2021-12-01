import math
import os


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = f.readlines()
    increments = -1
    previous = -math.inf
    for line in data:
        number = int(line)
        if number > previous:
            increments += 1
        previous = number

    return increments


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [int(x) for x in f.readlines()]
    increments = 0
    previous_sum = -math.inf
    # Got confused by the sample input with letters in it
    # ...you really use the exact same inputs as in part 1

    for i in range(len(data) - 2):
        triplet_sum = sum(data[i : i + 3])
        if i > 0 and triplet_sum > previous_sum:
            increments += 1
        previous_sum = triplet_sum

    return increments
