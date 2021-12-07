import os
from statistics import median


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        positions = [int(x) for x in f.readline().strip().split(",")]

    median_position = median(positions)

    return int(sum([abs(x - median_position) for x in positions]))


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        positions = [int(x) for x in f.readline().strip().split(",")]

    all_possibilities = []

    for converge_distance in range(min(positions), max(positions) + 1):
        fuel_cost = 0
        for position in positions:
            difference = abs(position - converge_distance)
            # https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
            fuel_cost += difference * (difference + 1) / 2

        all_possibilities.append(fuel_cost)

    return int(min(all_possibilities))
