import os
from typing import Dict, Tuple


def step(grid: Dict[Tuple[int, int], int], flash_sum: int = 0):
    for coordinates in grid:
        grid[coordinates] += 1

    flashing = [coordinates for coordinates, val in grid.items() if val > 9]

    while flashing:
        (x, y) = flashing.pop()
        neighbours = [
            coordinates
            for coordinates in [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
                (x + 1, y + 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x - 1, y - 1),
            ]
            if coordinates in grid
        ]
        grid[(x, y)] = -1
        flash_sum += 1

        for coordinates in neighbours:
            if -1 < grid[coordinates] < 10:
                grid[coordinates] += 1

        flashing.extend(
            [
                coordinates
                for coordinates, val in grid.items()
                if val > 9 and coordinates not in flashing
            ]
        )

    for coordinates in grid:
        if grid[coordinates] == -1:
            grid[coordinates] = 0

    return grid, flash_sum


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    total_flashes = 0
    grid = {}
    for y, row in enumerate(data):
        for x, column in enumerate(row):
            grid[(x, y)] = int(column)

    for i in range(100):
        grid, total_flashes = step(grid, total_flashes)

    return total_flashes


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    steps = 0
    grid = {}
    for y, row in enumerate(data):
        for x, column in enumerate(row):
            grid[(x, y)] = int(column)
    grid_sum = sum(grid.values())

    while grid_sum != 0:
        grid, _ = step(grid)

        steps += 1
        grid_sum = sum(grid.values())

    return steps
