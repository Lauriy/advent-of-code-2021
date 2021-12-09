from advent_of_code_2021.day_8 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_8_sample.txt")

    print(answer)
    assert answer == 26

    answer = solve_first("day_8_my_input.txt")

    print(answer)
    assert answer == 440


def test_solve_second():
    answer = solve_second("day_8_sample.txt")

    print(answer)
    assert answer == 61229

    answer = solve_second("day_8_my_input.txt")

    print(answer)
    assert answer == 1046281
