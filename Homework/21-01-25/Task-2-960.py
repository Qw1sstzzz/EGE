from itertools import *

def f(a, b, c):
    return (a and (not b)) or c


table = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]

if len(set(table)) == len(table):
    for p in permutations('abc'):
        u = [f(**dict(zip(p, t))) for t in table]
        if u == [0, 1, 1, 1, 0, 0, 1, 1]:
            print(*p)

# bca