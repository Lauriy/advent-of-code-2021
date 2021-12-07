import os
from collections import defaultdict, namedtuple
from typing import List

Line = namedtuple("Line", ["x1", "x2", "y1", "y2"])


def read_file(file_name: str) -> List[Line]:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    lines = []
    for p2p_line in data:
        line_parts = p2p_line.split(" -> ")
        start_coordinates = [int(x) for x in line_parts[0].split(",")]
        end_coordinates = [int(x) for x in line_parts[1].split(",")]
        line = Line(
            start_coordinates[0],
            end_coordinates[0],
            start_coordinates[1],
            end_coordinates[1],
        )
        lines.append(line)

    return lines


def get_visited_points(
    lines: List[Line], allow_diagonals=False
) -> defaultdict[int]:
    points_visited = defaultdict(int)
    for line in lines:
        dx = abs(line.x2 - line.x1)
        dy = abs(line.y2 - line.y1)
        if line.y1 == line.y2:
            min_x = min(line.x2, line.x1)
            for i in range(min_x, min_x + dx + 1):
                points_visited[(i, line.y1)] += 1
        elif line.x1 == line.x2:
            min_y = min(line.y2, line.y1)
            for i in range(min_y, min_y + dy + 1):
                points_visited[(line.x1, i)] += 1
        elif allow_diagonals:
            length = abs(line.x2 - line.x1)
            dx = (line.x2 - line.x1) / length
            dy = (line.y2 - line.y1) / length
            for n in range(length + 1):
                x = line.x1 + (dx * n)
                y = line.y1 + (dy * n)
                points_visited[(x, y)] += 1

    return points_visited


def solve_first(file_name: str) -> int:
    lines = read_file(file_name)

    return sum(1 for v in get_visited_points(lines).values() if v > 1)


def solve_second(file_name: str) -> int:
    lines = read_file(file_name)

    return sum(
        1
        for v in get_visited_points(lines, allow_diagonals=True).values()
        if v > 1
    )
