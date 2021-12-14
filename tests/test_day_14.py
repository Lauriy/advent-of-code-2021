from advent_of_code_2021.day_14 import lahenda_esimene_osa, lahenda_teine_osa


def test_lahenda_esimene_osa():
    vastus = lahenda_esimene_osa("day_14_sample.txt")

    print(vastus)
    assert vastus == 1588

    vastus = lahenda_esimene_osa("day_14_my_input.txt")

    print(vastus)
    assert vastus == 2223


def test_lahenda_teine_osa():
    vastus = lahenda_teine_osa("day_14_my_input.txt")

    print(vastus)
    assert vastus == 2566282754493
