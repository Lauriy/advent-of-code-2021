import math
import os
from typing import Dict, Tuple


def get_basin_recursively(
    x: int, y: int, height_map: Dict[Tuple[int, int], int]
):
    basin = [(x, y)]
    adjacent_points = [
        p
        for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if p in height_map
    ]

    if height_map[(x, y)] == 9:
        return []

    for (x2, y2) in adjacent_points:
        if height_map[(x2, y2)] > height_map[(x, y)]:
            basin.extend(get_basin_recursively(x2, y2, height_map))

    return basin


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    risk_sum = 0
    height_map = {
        (x, y): int(col)
        for y, row in enumerate(data)
        for x, col in enumerate(row)
    }
    for (x, y), val in height_map.items():
        adjacent_points = [
            p
            for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            if p in height_map
        ]
        all_higher = True
        for each in adjacent_points:
            if height_map[each] <= val:
                all_higher = False
                break

        if all_higher:
            risk_sum += val + 1

    return risk_sum


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    height_map = {
        (x, y): int(column)
        for y, row in enumerate(data)
        for x, column in enumerate(row)
    }

    basin_sizes = []
    for (x, y), val in height_map.items():
        adjacent_points = [
            p
            for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            if p in height_map
        ]

        all_higher = True
        for each in adjacent_points:
            if height_map[each] <= val:
                all_higher = False
                break

        if all_higher:
            points = set(get_basin_recursively(x, y, height_map))
            basin_sizes.append(len(points))

    return math.prod(sorted(basin_sizes)[-3:])
