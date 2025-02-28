from itertools import *

def f(H, L, W, N):
    return (not (H <= L)) <= ((not (W <= N)) and H)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [
        (0, 0, 0, a1),
        (0, 0, a2, a3),
        (0,a4, a5, a6)
    ]
    if len(set(table)) == len(table):
        for p in permutations('HLWN'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [0, 0, 0]:
                print(*p)

# LWNH