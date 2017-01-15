# A 0
# B 1
# C 2
# D 3
# E 4
# F 5
# G 6
# H 7
# I 8

servad = [
    (0, 1, 22),
    (0, 2, 9),
    (0, 3, 12),
    (1, 2, 35),
    (1, 5, 36),
    (1, 7, 34),
    (2, 5, 42),
    (2, 3, 4),
    (2, 4, 65),
    (3, 4, 33),
    (3, 8, 30),
    (4, 5, 18),
    (4, 6, 23),
    (5, 6, 39),
    (5, 7, 24),
    (6, 7, 25),
    (6, 8, 21),
    (7, 8, 19),
]

graaf = []
for i in range(9):
    graaf.append([])

for serv in servad:
    graaf[serv[0]].append((serv[1], serv[2]))
    graaf[serv[1]].append((serv[0], serv[2]))


def leia_lyhim(graaf, algus):
    from heapq import heappush
    from heapq import heappop
    import math

    kaugused = [math.inf] * len(graaf)
    kaugused[algus] = 0

    kaidud = [False] * len(graaf)

    kuhi = []
    heappush(kuhi, (0, algus))

    while kuhi:
        (kaugus_kokku, tipp) = heappop(kuhi)
        if kaidud[tipp]:
            continue
        kaidud[tipp] = True

        print((kaugus_kokku, tipp))

        naabrid = graaf[tipp]
        for (naaber, kaugus) in naabrid:
            seni_parim = kaugused[naaber]
            uus_kaugus = kaugus_kokku + kaugus
            if uus_kaugus < seni_parim:
                kaugused[naaber] = uus_kaugus
                heappush(kuhi, (uus_kaugus, naaber))


# leia_lyhim(graaf, 5)


def leia_lyhim_loop(graaf, algus):
    import math

    kaugused = [math.inf] * len(graaf)
    kaugused[algus] = 0

    kaidud = [False] * len(graaf)

    jarjekord = []
    jarjekord.append(algus)

    while jarjekord:
        tipp = jarjekord[0]
        for kandidaat in jarjekord:
            if kaugused[kandidaat] < kaugused[tipp]:
                tipp = kandidaat

        jarjekord.remove(tipp)
        if kaidud[tipp]:
            continue
        kaidud[tipp] = True
        kaugus_kokku = kaugused[tipp]
        print((kaugus_kokku, tipp))

        naabrid = graaf[tipp]
        for (naaber, kaugus) in naabrid:
            seni_parim = kaugused[naaber]
            uus_kaugus = kaugus_kokku + kaugus
            if uus_kaugus < seni_parim:
                kaugused[naaber] = uus_kaugus
                jarjekord.append(naaber)


leia_lyhim_loop(graaf, 0)
