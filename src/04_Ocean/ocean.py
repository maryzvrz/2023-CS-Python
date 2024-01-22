pole = [[3, 3, 3, 2, 1], [1, 0, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [3, 2, 1, 2, 3]]
old_pole = pole
width = len(pole)
length = len(pole[width - 1])
nraz = 1
two = 2
three = 3


def neight(i, j):
    neigh = []
    if i > 0 and j > 0:
        neigh.append(pole[i - 1][j - 1])
    if i > 0:
        neigh.append(pole[i - 1][j])
    if i > 0 and j < length - 1:
        neigh.append(pole[i - 1][j + 1])
    if j > 0:
        neigh.append(pole[i][j - 1])
    if j < length - 1:
        neigh.append(pole[i][j + 1])
    if i < width - 1 and j > 0:
        neigh.append(pole[i + 1][j - 1])
    if i < width - 1:
        neigh.append(pole[i + 1][j])
    if i < width - 1 and j < length - 1:
        neigh.append(pole[i + 1][j + 1])
    return str(neigh)


def replace(i, j):
    if pole[i][j] == 0:
        if fish == three:
            pole[i][j] = 2
        if shrimp == three:
            pole[i][j] = 3
        if fish == three and shrimp == three:
            pole[i][j] = 2
    if pole[i][j] == two:
        if fish < two or fish > three:
            pole[i][j] = 0
    if pole[i][j] == three:
        if shrimp < two or shrimp > three:
            pole[i][j] = 0
    return pole[i][j]


for _ in range(nraz):
    for i in range(width):
        for j in range(length):
            fish = neight(i, j).count("2")
            shrimp = neight(i, j).count("3")
            pole[i][j] = replace(i, j)
