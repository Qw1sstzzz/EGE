from itertools import *

alph = sorted(list(set('КАЛЕЙДОСКОП')), reverse=True)

res = []
for pos, val in enumerate(product(alph, repeat=6), start = 0):
    s = ''.join(val)
    if pos % 2 == 0:
        if (s[0] in 'К') and (s.count('Й') >= 2) and ((s.count('С') + s.count('Е')) == 0):
            res.append([pos, s])

print(min(res))