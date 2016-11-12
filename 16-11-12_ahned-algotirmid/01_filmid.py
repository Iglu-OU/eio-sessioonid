# Juku valis telekavast erinevatelt kanalitelt välja N filmi. Kahjuks avastas ta, et pajude filmise ajad kattuvad
# osaliselt. Ta tahab vaadata võimalikult palju filme, ilma, et ükski poolikuks jääks.

# Sisend: list filmide algusaja ja kestvuse paaridest
# Väljund: list valitud filmide indeksitest


import random

random.seed(0)


def random_film():
    algus = str(random.randrange(8, 23)).zfill(2) + ":" + str(random.randrange(0, 60, 5)).zfill(2)
    kestvus = str(random.randrange(1, 3)) + ":" + str(random.randrange(0, 60, 5)).zfill(2)
    return algus, kestvus


filmid = []

for _ in range(20):
    filmid.append(random_film())

print(filmid)
