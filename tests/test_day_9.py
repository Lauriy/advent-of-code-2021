from advent_of_code_2021.day_9 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_9_sample.txt")

    print(answer)
    assert answer == 15

    answer = solve_first("day_9_my_input.txt")

    print(answer)
    assert answer == 448


def test_solve_second():
    answer = solve_second("day_9_sample.txt")

    print(answer)
    assert answer == 1134

    answer = solve_second("day_9_my_input.txt")

    print(answer)
    assert answer == 1417248
