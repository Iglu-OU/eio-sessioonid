# Alati ei pea graaf olemal eelnevalt tervikuna defineeritud,
# piisab, kui me teame reegleid kuidas leida iga tipu naabrid


def ratsu_kaigud(algus):
    naabrid = []

    def append(x, y):
        uusX = ord(algus[0]) + x
        uusY = int(algus[1]) + y
        if uusX < ord('a') or uusX > ord('h'):
            return

        if uusY < 1 or uusY > 8:
            return

        naabrid.append(chr(uusX) + str(uusY))

    append(+ 2, + 1)
    append(+ 2, - 1)
    append(+ 1, + 2)
    append(+ 1, - 2)
    append(- 1, + 2)
    append(- 1, - 2)
    append(- 2, + 1)
    append(- 2, - 1)

    return naabrid


# print(ratsu_kaigud("h8"))


def lyhim_tee(algus, l6pp):
    from collections import deque
    q = deque()
    lisatud = set()

    q.append(algus)
    lisatud.add(algus)

    prev = dict()

    while q:
        tipp = q.popleft()

        if tipp == l6pp:
            print("kohal")
            print(tipp)
            while tipp in prev:
                print(prev[tipp])
                tipp = prev[tipp]
            return

        naabrid = ratsu_kaigud(tipp)
        for naaber in naabrid:
            if naaber not in lisatud:
                prev[naaber] = tipp
                q.append(naaber)
                lisatud.add(naaber)


# lyhim_tee("a1", "h8")


def teekond_koik_ruudud(algus):
    from collections import deque
    q = deque()
    lisatud = set()

    q.append(algus)
    lisatud.add(algus)

    prev = dict()
    tipp = None

    teekond = []
    while q:
        tipp = q.pop()
        # print("tipp: " + tipp)
        teekond.append(tipp)

        naabrid = ratsu_kaigud(tipp)
        for naaber in naabrid:
            if naaber not in lisatud:
                prev[naaber] = tipp
                q.append(naaber)
                lisatud.add(naaber)

    print(len(teekond))
    print(teekond)

#  teekond_koik_ruudud("a1")

def sidus_komp(etturid):
    from collections import deque
    q = deque()

    vaatamata = []
    for x in "abcdefgh":
        for y in "12345678":
            vaatamata.append(x + y)

    while vaatamata:
        algus = vaatamata.pop()
        if algus in etturid:
            continue
        print("Otsin komponenti alates " + algus)
        q.append(algus)
        komponent = []
        while q:
            tipp = q.pop()
            if tipp in etturid:
                continue
            komponent.append(tipp)
            naabrid = ratsu_kaigud(tipp)
            for naaber in naabrid:
                if naaber in vaatamata:
                    q.append(naaber)
                    vaatamata.remove(naaber)
        print(komponent)

sidus_komp(["h8", "b3", "c2", "b5", "c6", "e6", "f5", "e2", "f3", "g5", "f4", "f2"])
