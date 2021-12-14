import os
from collections import Counter, defaultdict


def lahenda_esimene_osa(failinimi: str, mitu_korda_asendada: int = 10) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{failinimi}", "r"
    ) as f:
        polymer, _, *asendused = f.read().split("\n")
    asendused = dict(asendus.split(" -> ") for asendus in asendused if asendus)

    k6rvuti_t2htede_loendur = Counter(
        esimene + teine for esimene, teine in zip(polymer, polymer[1:])
    )
    yldine_t2htede_loendur = Counter(polymer)
    for n in range(mitu_korda_asendada):
        uus_k6rvuti_loendur = defaultdict(int)

        for paar, esinemisi in k6rvuti_t2htede_loendur.items():
            lisa = asendused[paar]
            uus_k6rvuti_loendur[paar[0] + lisa] += esinemisi
            uus_k6rvuti_loendur[lisa + paar[1]] += esinemisi
            yldine_t2htede_loendur[lisa] += esinemisi

        k6rvuti_t2htede_loendur = uus_k6rvuti_loendur

    return max(yldine_t2htede_loendur.values()) - min(
        yldine_t2htede_loendur.values()
    )


def lahenda_teine_osa(failinimi: str, mitu_korda_asendada: int = 40) -> int:
    return lahenda_esimene_osa(failinimi, mitu_korda_asendada)
