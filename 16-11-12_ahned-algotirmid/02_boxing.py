import math

sisend = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6],
    [0, 1, 2],
    [1, 2, 3, 4, 5, 6, 7, 8],
]

sisend2 = [
    [100, 200, 300, 1200, 6000],
    [],
    [900, 902, 1200, 4000, 5000, 6001],
    [0, 2000, 6002],
    [1, 2, 3, 4, 5, 6, 7, 8],
]

sisend3 = [
    [5000, 6500],
    [6000],
    [6500],
    [6000],
    [0, 5800, 6000],
]


def uus_algus(sisend):
    sisend.sort(key=lambda kohtunik: kohtunik[0] if len(kohtunik) > 0 else math.inf)
    if (len(sisend[0]) == 0):
        return -1
    algus = sisend[0][0]
    return algus


def leia_veel(sisend, algus):
    leitud = 0
    for kohtunik in sisend:
        if (len(kohtunik) > 0 and kohtunik[0] < algus + 1000):
            leitud += 1
            if leitud == 3:
                return kohtunik[0]
    return -1


def eemalda(sisend, leitud):
    for kohtunik in sisend:
        while (len(kohtunik) and kohtunik[0] <= leitud):
            kohtunik.pop(0)


def boxing(sisend):
    tulemus = 0

    while True:
        algus = uus_algus(sisend)
        print("algus", algus)
        if (algus == -1):
            return tulemus
        leitud = leia_veel(sisend, algus)
        if leitud != -1:
            tulemus += 1
            eemalda(sisend, leitud)
        else:
            eemalda(sisend, algus)


print(boxing(sisend))
print(boxing(sisend2))
print(boxing(sisend3))
