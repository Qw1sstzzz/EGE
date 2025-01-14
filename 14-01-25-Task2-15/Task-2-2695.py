from itertools import *

def f(x, y, w, z):
    return (w or y) and (x <= (not z)) and (not w)

cnt = set()
for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (a1, 0, a2, 0),
        (1, a3, a4, a5),
        (1, 1, 0, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [1, 1, 1]:
                cnt.add(p)
print(len(cnt))

# 4