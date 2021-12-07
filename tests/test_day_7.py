from advent_of_code_2021.day_7 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_7_sample.txt")

    print(answer)
    assert answer == 37

    answer = solve_first("day_7_my_input.txt")

    print(answer)
    assert answer == 328318


def test_solve_second():
    answer = solve_second("day_7_sample.txt")

    print(answer)
    assert answer == 168

    answer = solve_second("day_7_my_input.txt")

    print(answer)
    assert answer == 89791146
