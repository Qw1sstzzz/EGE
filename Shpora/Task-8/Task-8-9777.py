from itertools import *

alph = sorted(set('КОМПЬЮТЕР'))
ans = []

for pos, i in enumerate(product(alph, repeat=5), start=1):
    s = ''.join(i)
    if pos % 2 != 0 and s[0] != 'Ь' and s.count('К') == 2:
        ans.append([pos, s])

print(max(ans))