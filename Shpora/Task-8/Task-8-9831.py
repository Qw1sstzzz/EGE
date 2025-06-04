from itertools import *

alph = '0123456789ABCDEF'
cnt = 0
for i in product(alph, repeat=3):
    s = ''.join(i)
    if s[0] != '0' and len(set(s)) == len(s):
        for c in '02468ACE':
            s = s.replace(c, '*')
        for j in '13579BDF':
            s = s.replace(j, '!')
        if '**' not in s and '!!' not in s:
            cnt += 1
print(cnt)