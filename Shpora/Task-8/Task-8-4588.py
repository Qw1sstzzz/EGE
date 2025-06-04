from itertools import *

alph = '01234567'
cnt = 0

for i in product(alph, repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('6') == 1:
        for c in '1357':
            s = s.replace(c, '*')
        if '*6' not in s and '6*' not in s:
            cnt += 1
print(cnt)