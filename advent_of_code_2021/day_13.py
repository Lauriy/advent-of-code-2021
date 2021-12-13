import math
import os


def voldi(telg: str, kust_voltida: int, koordinaadid: set) -> set:
    uued_koordinaadid = set()

    for x, y in koordinaadid:
        if telg == "x" and x > kust_voltida:
            x = 2 * kust_voltida - x
        elif telg == "y" and y > kust_voltida:
            y = 2 * kust_voltida - y
        uued_koordinaadid.add((x, y))

    return uued_koordinaadid


def joonista_tulemus(koordinaadid: set):
    suurim_x = -math.inf
    suurim_y = -math.inf
    for (x, y) in koordinaadid:
        if x > suurim_x:
            suurim_x = x
        if y > suurim_y:
            suurim_y = y

    x_piire = suurim_x + 1
    y_piire = suurim_y + 1

    ruudustik = [[" "] * x_piire for _ in range(y_piire)]

    for x, y in koordinaadid:
        ruudustik[y][x] = "#"

    print("\n", "\n".join("".join(rida) for rida in ruudustik), sep="")


def lahenda_esimene_osa(failinimi: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{failinimi}", "r"
    ) as f:
        k6ik_read = [x.strip() for x in f.readlines()]

    koordinaadid = set()
    voltimisjuhised = []
    for rida in k6ik_read:
        if "," in rida:
            koordinaadid.add(tuple(int(jupp) for jupp in rida.split(",")))
        elif "fold" in rida:
            voltimisjuhised.append(rida.split()[2].split("="))

    for telg, kust_voltida in voltimisjuhised[:1]:
        koordinaadid = voldi(telg, int(kust_voltida), koordinaadid)

    return len(koordinaadid)


def lahenda_teine_osa(failinimi: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{failinimi}", "r"
    ) as f:
        k6ik_read = [x.strip() for x in f.readlines()]

    koordinaadid = set()
    voltimisjuhised = []
    for rida in k6ik_read:
        if "," in rida:
            koordinaadid.add(tuple(int(jupp) for jupp in rida.split(",")))
        elif "fold" in rida:
            voltimisjuhised.append(rida.split()[2].split("="))

    for telg, kust_voltida in voltimisjuhised:
        koordinaadid = voldi(telg, int(kust_voltida), koordinaadid)

    print(joonista_tulemus(koordinaadid))
