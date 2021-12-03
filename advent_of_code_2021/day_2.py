import os


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = f.readlines()
    position = [0, 0]
    for command in data:
        match command.split():
            case ["forward", units]:
                position[0] += int(units)
            case ["down", units]:
                position[1] += int(units)
            case ["up", units]:
                position[1] -= int(units)

    return position[0] * position[1]


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    position = [0, 0, 0]

    for command in data:
        match command.split():
            case ["forward", units]:
                number = int(units)
                position[0] += number
                position[1] += number * position[2]
            case ["down", units]:
                position[2] += int(units)
            case ["up", units]:
                position[2] -= int(units)

    return position[0] * position[1]
