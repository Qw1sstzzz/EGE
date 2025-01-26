from itertools import *

def f1(w, x, y, z):
    return (w == x) and (y <= z)

def f2(w, x, y, z):
    return (w <= x) <= (y == z)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (1, a1, 1, 1, 1, 0),
        (a2, 1, 0, 0, 1, a3),
        (a4, 0, 0, a5, 0, 0)
    ]

    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            u1 = [f1(**dict(zip(p, t))) for t in table]
            u2 = [f2(**dict(zip(p, t))) for t in table]

            if u1 == [1, 1, 0] and u2 == [0, a3, 0]:
                print(*p)

# zywx