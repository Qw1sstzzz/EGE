from itertools import *

alph = '012345678'
cnt = 0
for i in product(alph, repeat=5):
    s = ''.join(i)
    t = s
    if s[0] != '0' and s.count('0') == 1:
        for c in '1357':
            t = t.replace(c, '*')
        if '*0' not in t and '0*' not in t:
            cnt += 1
print(cnt)