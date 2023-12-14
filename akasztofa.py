import random

def szo_valaszto():
    with open("szavak.txt", "r", encoding="utf-8") as file:
        szavak = file.read().splitlines()
    return random.choice(szavak)


