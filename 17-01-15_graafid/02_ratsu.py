
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


print(ratsu_kaigud("h8"))
