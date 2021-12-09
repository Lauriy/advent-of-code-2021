import os


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
