from itertools import *

alph = sorted(set('ЛУНАТИК'))
print(alph)
ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] == 'Н':
        gl_cnt = len([i for i in val if i in 'УАИ'])
        if gl_cnt == 1:
            ans.append([pos, val])
print(max(ans))