from itertools import *

alph = '0123456789'
chet = '02468'
cnt = 0

for val in product(alph, repeat=6):
    s = ''.join(val)
    if (s[0] != '0') and (int(s) % 4 == 0) and (len(set(s)) == len(s)):
        for c in chet:
            s = s.replace(c, '*')
        if '**' not in s:
            cnt += 1
print(cnt)