from advent_of_code_2021.day_1 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_1_sample.txt")

    print(answer)
    assert answer == 7

    answer = solve_first("day_1_my_input.txt")

    print(answer)
    assert answer == 1676


def test_solve_second():
    answer = solve_second("day_1_sample.txt")

    print(answer)
    assert answer == 5

    answer = solve_second("day_1_my_input.txt")

    print(answer)
    assert answer == 1706
