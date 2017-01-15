# naabrusnimistu (adjacency list)

# Nädisigraaf, http://lehtmets.iglu.ee/AA_kogu_15dets_kell_1515.pdf Joonis 19, lk 84
tipud = ["a", "b", "c", "d", "e", "f", "g", "h"]
graaf = [
    [1, 2, 3],  # tipp a
    [2],  # tipp b
    [4],  # tipp c
    [5, 6],  # tipp d
    [7],  # tipp e
    [7],  # tipp f
    [7],  # tipp g,
    [],  # tipp h
]

kaidud = [False] * len(graaf)

def sygav_rekurs(graaf, tipp):

    print(tipud[tipp])

    naabrid = graaf[tipp]
    for naaber in naabrid:
        if not kaidud[naaber]:
            kaidud[naaber] = True
            sygav_rekurs(graaf, naaber)


print("Sügavuti")
sygav_rekurs(graaf, 0)


# kasutame pythoni standard teekides olevat järjekorra implementatsiooni
from collections import deque

# Graafi laiuti läbimine kasutades järjekorda
def laiuti(graaf, algus):
    lisatud = [False] * len(graaf)
    jarjekord = deque()
    jarjekord.append(algus)
    lisatud[algus] = True

    while jarjekord:
        tipp = jarjekord.pop()

        print(tipud[tipp])

        naabrid = graaf[tipp]
        for naaber in naabrid:
            if not lisatud[naaber]:
                jarjekord.append(naaber)
                lisatud[naaber] = True


print ("Laiuti:")
laiuti(graaf, 0)

