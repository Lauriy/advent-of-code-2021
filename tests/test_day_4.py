from typing import List

import pytest

from advent_of_code_2021.day_4 import check_if_board_won, solve_first


@pytest.mark.parametrize(
    "board, expected_result",
    [
        (
            [
                [
                    ("22", False),
                    ("13", False),
                    ("17", False),
                    ("11", False),
                    ("0", False),
                ],
                [
                    ("8", False),
                    ("2", False),
                    ("23", False),
                    ("4", False),
                    ("24", False),
                ],
                [
                    ("21", False),
                    ("9", False),
                    ("14", False),
                    ("16", False),
                    ("7", False),
                ],
                [
                    ("6", False),
                    ("10", False),
                    ("3", False),
                    ("18", False),
                    ("5", False),
                ],
                [
                    ("1", False),
                    ("12", False),
                    ("20", False),
                    ("15", False),
                    ("19", False),
                ],
            ],
            False,
        ),
        (
            [
                [
                    ("22", True),
                    ("13", True),
                    ("17", True),
                    ("11", True),
                    ("0", True),
                ],
                [
                    ("8", False),
                    ("2", False),
                    ("23", False),
                    ("4", False),
                    ("24", False),
                ],
                [
                    ("21", False),
                    ("9", False),
                    ("14", False),
                    ("16", False),
                    ("7", False),
                ],
                [
                    ("6", False),
                    ("10", False),
                    ("3", False),
                    ("18", False),
                    ("5", False),
                ],
                [
                    ("1", False),
                    ("12", False),
                    ("20", False),
                    ("15", False),
                    ("19", False),
                ],
            ],
            True,
        ),
        (
            [
                [
                    ("22", True),
                    ("13", False),
                    ("17", False),
                    ("11", False),
                    ("0", False),
                ],
                [
                    ("8", True),
                    ("2", False),
                    ("23", False),
                    ("4", False),
                    ("24", False),
                ],
                [
                    ("21", True),
                    ("9", False),
                    ("14", False),
                    ("16", False),
                    ("7", False),
                ],
                [
                    ("6", True),
                    ("10", False),
                    ("3", False),
                    ("18", False),
                    ("5", False),
                ],
                [
                    ("1", True),
                    ("12", False),
                    ("20", False),
                    ("15", False),
                    ("19", False),
                ],
            ],
            True,
        ),
    ],
)
def test_check_if_board_won(board: List[List], expected_result):
    assert check_if_board_won(board) == expected_result


def test_solve_first():
    answer = solve_first("day_4_sample.txt")

    print(answer)
    assert answer == 4512

    answer = solve_first("day_4_my_input.txt")

    print(answer)
    assert answer == 65325
