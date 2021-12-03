from advent_of_code_2021.day_2 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_2_sample.txt")

    assert answer == 150
    print(answer)

    answer = solve_first("day_2_my_input.txt")

    assert answer == 1714950
    print(answer)


def test_solve_second():
    answer = solve_second("day_2_sample.txt")

    assert answer == 900
    print(answer)

    answer = solve_second("day_2_my_input.txt")

    # assert answer == 1714950
    print(answer)
