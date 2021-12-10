from advent_of_code_2021.day_10 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_10_sample.txt")

    print(answer)
    assert answer == 26397

    answer = solve_first("day_10_my_input.txt")

    print(answer)
    assert answer == 442131


def test_solve_second():

    answer = solve_second("day_10_sample.txt")

    print(answer)
    assert answer == 288957

    answer = solve_second("day_10_my_input.txt")

    print(answer)
    assert answer == 3646451424
