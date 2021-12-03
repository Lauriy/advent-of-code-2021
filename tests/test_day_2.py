from advent_of_code_2021.day_2 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_2_sample.txt")

    print(answer)
    assert answer == 150

    answer = solve_first("day_2_my_input.txt")

    print(answer)
    assert answer == 1714950


def test_solve_second():
    answer = solve_second("day_2_sample.txt")

    print(answer)
    assert answer == 900

    answer = solve_second("day_2_my_input.txt")

    print(answer)
    assert answer == 1281977850
