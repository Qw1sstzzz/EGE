from itertools import *

def f(x, y, z, w):
    return (w <= (y == z)) and (y == (z <= x))

for a1, a2 in product([0, 1], repeat=2):
    table = [
        (a1, 0, 0, 0),
        (0, a2, 1, 1),
        (0, 0, 0, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [1, 1, 0]:
                print(*p)