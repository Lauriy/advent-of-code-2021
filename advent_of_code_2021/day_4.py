import os
from typing import List


def check_if_board_won(board: List[List]) -> bool:
    for i in range(len(board)):
        true_count = 0
        row_size = len(board[i])
        for j in range(row_size):
            if board[i][j][1]:
                true_count += 1
            if true_count == row_size:
                return True
    column_size = len(board)
    for i in range(column_size):
        true_count = 0
        for j in range(column_size):
            if board[j][i][1]:
                true_count += 1
            if true_count == column_size:
                return True

    return False


def mark_boards(boards: List[List[List]], pick: str) -> List[List[List]]:
    for board in boards:
        for line in board:
            for square in line:
                if square[0] == pick:
                    square[1] = True

    return boards


def board_unmarked_sum(board: List[List]) -> int:
    board_sum = 0
    for line in board:
        for symbol in line:
            if not symbol[1]:
                board_sum += int(symbol[0])

    return board_sum


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    is_first = True
    boards = []
    i = -1
    number_to_win_it = None
    unmarked_sum = 0
    picks = []
    for line in data:
        if is_first:
            picks = line.split(",")
            is_first = False
            continue
        if not line:
            boards.append([])
            i += 1
            continue
        boards[i].append([[x, False] for x in line.split()])
    for pick in picks:
        boards = mark_boards(boards, pick)
        for board in boards:
            if check_if_board_won(board):
                number_to_win_it = pick
                unmarked_sum = board_unmarked_sum(board)
                break
        if unmarked_sum:
            break

    return int(number_to_win_it) * unmarked_sum
