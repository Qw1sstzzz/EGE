from itertools import *

alph = sorted(set('АРГУМЕНТ'))
ans = []

for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if len(set(val)) == len(val):
        if val[0] <= val[1] <= val[2] <= val[3]:
            ans.append([pos, val])
print(max(ans))