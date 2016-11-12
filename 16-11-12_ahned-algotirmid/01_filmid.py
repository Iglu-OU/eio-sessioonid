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

filmid = [
    ('21:30', '2:00'),
    ('12:40', '2:30'),
    ('22:20', '2:25'),
    ('17:15', '1:20'),
    ('10:05', '2:40'),
    ('19:45', '1:20'),
    ('09:55', '1:50'),
    ('13:35', '1:25'),
    ('14:25', '1:40'),
    ('15:35', '2:00'),
    ('20:40', '1:05'),
    ('19:30', '1:45'),
    ('15:25', '1:55'),
    ('13:55', '1:15'),
    ('22:45', '1:15'),
    ('20:10', '2:05'),
    ('09:25', '2:05'),
    ('12:40', '2:55'),
    ('09:40', '2:40'),
    ('11:45', '2:35')
]

print(filmid)


def minutid(kellaaeg):
    split = kellaaeg.split(":")
    return int(split[0]) * 60 + int(split[1])


print(minutid("10:30"))


def l6pp(film):
    algus = film[0]
    kestvus = film[1]
    return minutid(algus) + minutid(kestvus)


print(l6pp(filmid[0]))


def sorteeri(filmid):
    koos_l6puga = []
    for film in filmid:
        koos_l6puga.append((l6pp(film), film[0], film[1]))
    koos_l6puga.sort(key=lambda film: film[0])
    return koos_l6puga


print(sorteeri(filmid))


def vali_filmid(filmid):
    valitud = []
    valitud_indeksid = []
    filmid = sorteeri(filmid)
    l6pp = 0

    for i, film in enumerate(filmid):
        algus = film[1]
        if (minutid(algus) > l6pp):
            valitud.append(film)
            valitud_indeksid.append(i)
            l6pp = film[0]

    return valitud


print(vali_filmid(filmid))
print(len(vali_filmid(filmid)))
