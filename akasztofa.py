import random

def szo_valaszto():
    with open("szavak.txt", "r", encoding="utf-8") as file:
        szavak = file.read().splitlines()
    return random.choice(szavak)


def szo_ki_iro(szo, kitalalt_betuk):
    kimutatás = ""
    for betu in szo:
        if betu in kitalalt_betuk:
            kimutatás += betu
        else:
            kimutatás += "_"
    return kimutatás


