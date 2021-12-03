import os
from typing import List


def mcb_str(bit_str_list: List[str]) -> str:
    single_str_length = len(bit_str_list[0])
    true_bit_counts = [0] * single_str_length
    strings_to_check = len(bit_str_list)
    to_win = strings_to_check / 2
    for i in range(strings_to_check):
        for j in range(single_str_length):
            if bit_str_list[i][j] == "1":
                true_bit_counts[j] += 1
    answer = ""
    for each in true_bit_counts:
        if each > to_win:
            answer += "1"
        else:
            answer += "0"

    return answer


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    most_common_string = mcb_str(data)
    least_common_string = "".join(
        ["1" if x == "0" else "0" for x in most_common_string]
    )
    mcb_value = int(most_common_string, 2)
    lcb_value = int(least_common_string, 2)

    return mcb_value * lcb_value


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    single_str_length = len(data[0])
    oxygen_generator_candidates = data
    co2_scrubber_candidates = data
    for i in range(single_str_length):
        count = [0, 0]
        for each in oxygen_generator_candidates:
            if each[i] == "1":
                count[0] += 1
            else:
                count[1] += 1
        if count[0] >= count[1]:
            oxygen_generator_candidates = [
                x for x in oxygen_generator_candidates if x[i] == "1"
            ]
        else:
            oxygen_generator_candidates = [
                x for x in oxygen_generator_candidates if x[i] == "0"
            ]

        if len(oxygen_generator_candidates) == 1:
            break

    for i in range(single_str_length):
        count = [0, 0]
        for each in co2_scrubber_candidates:
            if each[i] == "0":
                count[0] += 1
            else:
                count[1] += 1
        if count[0] <= count[1]:
            co2_scrubber_candidates = [
                x for x in co2_scrubber_candidates if x[i] == "0"
            ]
        else:
            co2_scrubber_candidates = [
                x for x in co2_scrubber_candidates if x[i] == "1"
            ]

        if len(co2_scrubber_candidates) == 1:
            break

    return int(oxygen_generator_candidates[0], 2) * int(
        co2_scrubber_candidates[0], 2
    )
