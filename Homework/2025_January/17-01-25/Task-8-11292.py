from string import digits, ascii_uppercase
from itertools import *

alph = (digits + ascii_uppercase)[:16]

cnt = 0
for val in product(alph, repeat=5):
    s = ''.join(val)
    if s[0] != '0' and s.count('6') == 2:
        for c in '0248ACE':
            s = s.replace(c, '*')
        if '6*' not in s and '*6' not in s and '66' not in s:
            cnt += 1
print(cnt)

# 4352