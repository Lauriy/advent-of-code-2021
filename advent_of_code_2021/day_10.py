import os

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
pairs = {")": "(", "]": "[", "}": "{", ">": "<"}

scores_part_2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def grade_line(line: str) -> int:
    stack = []
    for symbol in line:
        if symbol in "([{<":
            stack.append(symbol)
        else:
            top = stack.pop() if stack else None
            if top != pairs[symbol]:
                return scores[symbol]

    return 0


def grade_line_part_2(line: str) -> int:
    stack = []
    for symbol in line:
        if symbol in "([{<":
            stack.append(symbol)
        else:
            top = stack.pop() if stack else None
            if top != pairs[symbol]:
                return 0

    completion_score = 0
    for symbol in reversed(stack):
        completion_score *= 5
        completion_score += scores_part_2[symbol]

    return completion_score


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]

    return sum(([grade_line(line) for line in data]))


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]

    line_scores = [grade_line_part_2(line) for line in data]
    incompletes = sorted([score for score in line_scores if score])

    return incompletes[int(len(incompletes) / 2)]
