import decimal
import os
from collections import defaultdict, namedtuple
from decimal import Decimal


def lin_equ(l1, l2):
    """https://stackoverflow.com/questions/21565994/
    method-to-return-the-equation-of-a-straight-line-given-two-points"""
    try:
        m = Decimal((l2[1] - l1[1])) / Decimal(l2[0] - l1[0])
    except decimal.DivisionByZero:
        m = 0
    c = l2[1] - (m * l2[0])

    return m, c


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    # max_x = 0
    # max_y = 0
    # lines_data = []
    # field = []
    points_visited = defaultdict(int)
    Line = namedtuple("Line", ["x1", "x2", "y1", "y2"])
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
        # equation = lin_equ(start_coordinates, end_coordinates)
        # lines_data.append({'start': start_coordinates,
        # 'end': end_coordinates, 'equation': equation})
        dx = abs(line.x2 - line.x1)
        dy = abs(line.y2 - line.y1)
        if dx and dy:
            # Skip diagonal movement
            continue
        if dx:
            min_x = min(line.x2, line.x1)
            for i in range(min_x, min_x + dx + 1):
                points_visited[(i, line.y1)] += 1
        elif dy:
            min_y = min(line.y2, line.y1)
            for i in range(min_y, min_y + dy + 1):
                points_visited[(line.x1, i)] += 1

    return sum(1 for v in points_visited.values() if v > 1)
    # lines_data.append({'start': start_coordinates,
    # 'end': end_coordinates, 'dx': dx, 'dy': dy})

    #     if start_coordinates[0] > max_x:
    #         max_x = start_coordinates[0]
    #     if end_coordinates[0] > max_x:
    #         max_y = end_coordinates[0]
    #     if start_coordinates[1] > max_y:
    #         max_y = start_coordinates[1]
    #     if end_coordinates[1] > max_y:
    #         max_y = end_coordinates[1]
    # for i in range(max_y + 1):
    #     field.append([])
    #     field[i] = [0] * (max_x + 1)
    # for each in lines_data:
    #     start_x = each['start'][0]
    #     start_y = each['start'][1]
    #     end_x = each['end'][0]
    #     end_y = each['end'][1]
    #     x_movement = abs(end_x - start_x)
    #     y_movement = abs(end_y - start_y)
    #     if x_movement and y_movement:
    #         # Skip diagonal movement
    #         continue
    #     print(start_x, start_y, end_x, end_y)
    #     print(x_movement, y_movement)
    #     if y_movement > 0:
    #         if start_y > end_y:
    #             modifier = -1
    #         else:
    #             modifier = 1
    #         for i in range(y_movement + 1):
    #             field[start_y - (i * modifier)][start_x] += 1
    #     elif x_movement > 0:
    #         if start_x > end_x:
    #             modifier = -1
    #         else:
    #             modifier = 1
    #         for i in range(x_movement + 1):
    #             field[start_y][start_x + (i * modifier)] += 1
    #     print(field)
    # at_least_two_seen = 0
    # for row in field:
    #     for column in row:
    #         if column > 1:
    #             at_least_two_seen += 1
    #
    # return at_least_two_seen
    # for each in lines_data:
    #     if each['equation'][0] != 0:
    #         # Only consider vertical/horizontal
    #         continue
    #     print(each)
    #     if each['start'][0] < each['end'][0]:
    #         for x in range(each['start'][0], each['end'][0] + 1):
    #             calculated_y = each['equation'][0] * x + each['equation'][1]
    #             field[int(calculated_y)][x] += 1
    #     else:
    #         for x in range(each['end'][0], each['start'][0] + 1):
    #             calculated_y = each['equation'][0] * x + each['equation'][1]
    #             field[int(calculated_y)][x] += 1
    # print(field)
