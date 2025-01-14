from itertools import *

def f(x, y, w, z):
    return (not ((not (x <= (not w))) and z)) and (not (w <= z)) and (x <= (not z))
cnt = set()
for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (1, 0, a1, 0),
        (1, 0, a2, a3),
        (a4, 1, a5, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [1, 0, 0]:
                cnt.add(p)
print(len(cnt))

# 8