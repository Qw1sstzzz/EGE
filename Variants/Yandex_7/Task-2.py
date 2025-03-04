from itertools import *

def f(w, x, y, z):
    return ((1 == w) == (not ((w and x) or y))) <= z

for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 in product([0, 1], repeat=10):
    table = [
        (a1, a2, 1, a3),
        (1, a4, 1, a5),
        (0, 1, 0, 0),
        (1, a6, 1, a7),
        (a8, a9, 1, a10)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [0, 0, 1, 1, 1]:
                print(*p)
                break