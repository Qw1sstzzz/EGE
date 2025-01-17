from itertools import *


def f(y, x, z, w):
    return (x == (not y)) <= ((x and w) == (z and (not w)))


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [
        (1, 1, a1, 1),
        (a2, 1, 1, a3),
        (0, a4, a5, a6)
    ]

    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [0, 0, 0]:
                print(*p)

# wzyx