from random import choice

szavak: list = []

def beolvas(filename):
    file = open(filename, 'r', encoding='UTF8')
    for sor in file:
        szavak.append(sor.strip())
    file.close()


def randomszo(szavak: list):
   szo = choice(szavak)
   return szo

def bontas(szo: str):
    for betu in szo:
        print('_', end=' ')
          


