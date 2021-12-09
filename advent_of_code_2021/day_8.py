import os
from typing import List

unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}


def extract_lexicographic_data(file_name: str) -> (List[str], List[str]):
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = f.readlines()

    patterns = []
    digits = []
    for line in data:
        line_data = line.strip().split(" | ")
        line_patterns, line_digits = line_data[0].split(), line_data[1].split()
        patterns += ["".join(sorted(x)) for x in line_patterns]
        digits += ["".join(sorted(x)) for x in line_digits]

    return patterns, digits


def solve_first(file_name: str) -> int:
    mapping = {}
    count = 0
    patterns, digits = extract_lexicographic_data(file_name)
    for pattern in patterns:
        length = len(pattern)
        if length in unique_lengths:
            number = unique_lengths[length]
            mapping[pattern] = number

    for digit in digits:
        if digit in mapping:
            count += 1

    return count


def solve_second(file_name: str) -> int:
    mapping = {}
    mapping_lookup = {}
    sum_of_outputs = 0
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = f.readlines()

    for line in data:
        line_data = line.strip().split(" | ")
        line_patterns, line_digits = line_data[0].split(), line_data[1].split()
        patterns = ["".join(sorted(x)) for x in line_patterns]
        digits = ["".join(sorted(x)) for x in line_digits]

        for pattern in patterns:
            length = len(pattern)
            if length in unique_lengths:
                number = unique_lengths[length]
                mapping[pattern] = number
                mapping_lookup[number] = set(pattern)

        for pattern in patterns:
            length = len(pattern)
            pattern_as_set = set(pattern)

            if length == 6:  # 0, 6, 9
                if not mapping_lookup[1].issubset(pattern_as_set):
                    mapping[pattern] = 6
                elif mapping_lookup[4].issubset(pattern_as_set):
                    mapping[pattern] = 9
                else:
                    mapping[pattern] = 0
            elif length == 5:  # 2, 3, 5
                if mapping_lookup[1].issubset(pattern_as_set):
                    mapping[pattern] = 3
                elif mapping_lookup[4] | pattern_as_set == mapping_lookup[8]:
                    mapping[pattern] = 2
                else:
                    mapping[pattern] = 5

        sum_of_outputs += int(
            "".join([str(mapping[digit]) for digit in digits])
        )

    return sum_of_outputs
