from advent_of_code_2021.day_13 import lahenda_esimene_osa, lahenda_teine_osa


def test_lahenda_esimene_osa():
    vastus = lahenda_esimene_osa("day_13_sample.txt")

    print(vastus)
    assert vastus == 17

    vastus = lahenda_esimene_osa("day_13_my_input.txt")

    print(vastus)
    assert vastus == 765


def test_lahenda_teine_osa():
    vastus = lahenda_teine_osa("day_13_my_input.txt")

    print(vastus)  # RZKZLPGH
