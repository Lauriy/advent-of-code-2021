from advent_of_code_2021.day_12 import solve_first, solve_second


def test_solve_first():
    answer = solve_first("day_12_sample_1.txt")

    print(answer)
    assert answer == 10

    answer = solve_first("day_12_sample_2.txt")

    print(answer)
    assert answer == 19

    answer = solve_first("day_12_sample_3.txt")

    print(answer)
    assert answer == 226

    answer = solve_first("day_12_my_input.txt")

    print(answer)
    assert answer == 4378


def test_solve_second():
    answer = solve_second("day_12_sample_1.txt")

    print(answer)
    assert answer == 36

    answer = solve_second("day_12_sample_2.txt")

    print(answer)
    assert answer == 103

    answer = solve_second("day_12_sample_3.txt")

    print(answer)
    assert answer == 3509

    answer = solve_second("day_12_my_input.txt")

    print(answer)
    # assert answer == 4378
