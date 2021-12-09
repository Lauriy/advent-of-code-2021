from advent_of_code_2021.day_9 import solve_first


def test_solve_first():
    answer = solve_first("day_9_sample.txt")

    print(answer)
    assert answer == 15

    answer = solve_first("day_9_my_input.txt")

    print(answer)
    assert answer == 448
