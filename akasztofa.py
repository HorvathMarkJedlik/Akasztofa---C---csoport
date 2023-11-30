szavak: list = []

def beolvas(filename):
    file = open(filename, 'r', encoding='UTF8')
    for sor in file:
        szavak.append(sor.strip())
    file.close()



beolvas('szavak.txt')
print(szavak)
