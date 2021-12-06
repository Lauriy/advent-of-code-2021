from advent_of_code_2021.day_5 import solve_first


def test_solve_first():
    answer = solve_first("day_5_sample.txt")

    print(answer)
    assert answer == 5

    answer = solve_first("day_5_my_input.txt")

    print(answer)
    assert answer == 6666
