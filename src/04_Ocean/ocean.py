import numpy as np

pole = np.matrix(
    [[3, 3, 3, 2, 1], [1, 0, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [3, 2, 1, 2, 3]]
)

width, length = pole.shape
nraz = 1
raz = 0
two = 2
three = 3


def neight(pole):
    neigh = []
    if i > 0 and j > 0:
        neigh.append(pole[i - 1, j - 1])
    if i > 0:
        neigh.append(pole[i - 1, j])
    if i > 0 and j < length - 1:
        neigh.append(pole[i - 1, j + 1])
    if j > 0:
        neigh.append(pole[i, j - 1])
    if j < length - 1:
        neigh.append(pole[i, j + 1])
    if i < width - 1 and j > 0:
        neigh.append(pole[i + 1, j - 1])
    if i < width - 1:
        neigh.append(pole[i + 1, j])
    if i < width - 1 and j < length - 1:
        neigh.append(pole[i + 1, j + 1])
    return str(neigh)


for _ in range(nraz):
    for i in range(width):
        for j in range(length):
            fish = neight(pole).count("2")
            shrimp = neight(pole).count("3")
            if pole[i, j] == 0:
                if fish == three:
                    pole[i, j] = 2
                if shrimp == three:
                    pole[i, j] = 3
                if fish == three and shrimp == three:
                    pole[i, j] = 2
            if pole[i, j] == two:
                if fish < two or fish > three:
                    pole[i, j] = 0
            if pole[i, j] == three:
                if shrimp < two or shrimp > three:
                    pole[i, j] = 0
