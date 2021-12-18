from advent_of_code_2021.day_11 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_11_sample.txt")

    print(answer)
    assert answer == 1656

    answer = solve_first("day_11_my_input.txt")

    print(answer)
    assert answer == 1725


def test_solve_second():
    answer = solve_second("day_11_sample.txt")

    print(answer)
    assert answer == 195

    answer = solve_second("day_11_my_input.txt")

    print(answer)
    assert answer == 308
