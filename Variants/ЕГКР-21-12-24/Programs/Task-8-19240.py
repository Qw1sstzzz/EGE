from itertools import *

res = []
alph = sorted('ЯНВАРЬ')
for idx, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] != 'Я' and val.count('Ь')  <= 1 and 'ЯЯ' not in val:
        res.append([idx, val])
print(max(res))

# 6406