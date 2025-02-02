from itertools import *

def f(w, y, x, z):
    return (w and y) or ((x <= w) == (y <= z))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [
        (a1, a2, a3, 1),
        (1, a4, a5, 1),
        (1, a6, 1, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [0, 0, 0]:
                print(*p)

# zwyx