from advent_of_code_2021.day_1 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_1_1_sample.txt")

    assert answer == 7
    print(answer)

    answer = solve_first("day_1_1_my_input.txt")

    assert answer == 1676
    print(answer)


def test_solve_second():
    answer = solve_second("day_1_1_sample.txt")

    assert answer == 5
    print(answer)

    answer = solve_second("day_1_1_my_input.txt")

    assert answer == 1706
    print(answer)
