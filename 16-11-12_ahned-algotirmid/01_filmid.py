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
