from itertools import product

alph = sorted('МАРКСЛ')
res = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    s = ''.join(val)
    if ('КС' not in s) and ('СК' not in s):
        t = [s.count(i) for i in s]
        if (t.count(1) == 3) and (t.count(3) == 3):
            res.append([pos, s])
print(max(res))

# 46605