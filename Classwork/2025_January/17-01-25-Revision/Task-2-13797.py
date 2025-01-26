# 1 способ

"""

print('w z y x f')
for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                f = ((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))
                if f == 1:
                    print(w, z, y, x, int(f))

# ywxz

"""

###############################################################################################

from itertools import *

def f(x, z, y, w):
    return ((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [
        (1, 0, 0, 0),
        (a1, 1, 0, a2),
        (1, 0, a3, a4)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table]
            if u == [1, 1, 1]:
                print(*p)

# ywxz