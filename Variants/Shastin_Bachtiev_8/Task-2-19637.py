from itertools import *

def f(z, x, w, y):
    return (z <= x) and ((x and (y == (not z))) <= w)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (a1, 1, 1, a2),
        (0, 0, a3, a4),
        (a5, 0, 0, 0)
    ]

    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [0, 0, 0]:
                print(*p)