from advent_of_code_2021.day_3 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_3_sample.txt")

    print(answer)
    assert answer == 198

    answer = solve_first("day_3_my_input.txt")

    print(answer)
    assert answer == 3320834


def test_solve_second():
    answer = solve_second("day_3_sample.txt")

    print(answer)
    assert answer == 230

    answer = solve_second("day_3_my_input.txt")

    print(answer)
    assert answer == 4481199
