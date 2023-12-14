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

def akasztófa():
    random_szo = szo_valaszto()
    kitalalt_betuk = []
    probalkozasok_szama = 6

    print("Üdvözöllek az Akasztófa játékban!")
    print(szo_ki_iro(random_szo, kitalalt_betuk))

    while probalkozasok_szama > 0:
        tipp = input("Adj meg egy betűt: ").lower()

        kitalalt_betuk.append(tipp)

        if tipp not in random_szo:
            probalkozasok_szama -= 1
            print(f"Hibás tipp! {probalkozasok_szama} próbálkozásod maradt.")
        else:
            print("Helyes tipp!")
            print(f"{probalkozasok_szama} próbálkozásod van még.")

        aktualis_allapot = szo_ki_iro(random_szo, kitalalt_betuk)
        print(aktualis_allapot)

        if "_" not in aktualis_allapot:
            print("Gratulálok, kitaláltad a szót!")
            break

    if probalkozasok_szama == 0:
        print(f"Sajnálom, vesztettél. A szó: {random_szo}")
