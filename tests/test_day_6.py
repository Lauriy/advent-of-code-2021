from advent_of_code_2021.day_6 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_6_sample.txt", 18)

    print(answer)
    assert answer == 26

    answer = solve_first("day_6_sample.txt", 80)

    print(answer)
    assert answer == 5934

    answer = solve_first("day_6_my_input.txt", 80)

    print(answer)
    assert answer == 360268


def test_solve_second():
    answer = solve_second("day_6_sample.txt", 256)

    print(answer)
    assert answer == 26984457539

    answer = solve_second("day_6_my_input.txt", 256)

    print(answer)
    assert answer == 1632146183902
