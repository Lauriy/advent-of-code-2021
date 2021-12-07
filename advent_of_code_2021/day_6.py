import os
from collections import Counter


def solve_first(file_name: str, days: int) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        initial_fishes = [int(x) for x in f.readline().strip().split(",")]
    counter = Counter(initial_fishes)
    for day in range(days):
        ready_to_give_birth_be_born = counter[0]
        for i in range(1, 9):
            counter[i - 1] = counter[i]
        counter[8] = ready_to_give_birth_be_born
        counter[6] += ready_to_give_birth_be_born

    return sum(counter.values())


def solve_second(file_name: str, days: int) -> int:
    return solve_first(file_name, days)
