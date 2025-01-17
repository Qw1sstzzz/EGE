from itertools import *

def f(y, x, z, w):
    return w and ((x or y) == (z and x))

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (1, a1, 1, 0),
        (0, a2, a3, a4),
        (1, 1, 1, a5)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [1, 1, 0]:
                print(*p)

# zywx