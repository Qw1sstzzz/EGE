from itertools import *

alph = '01234'
cnt = 0

for val in product(alph, repeat=6):
    s = ''.join(val)
    if s[0] != '0' and s[0] == '3':
        if s[-1] in '024':
            cnt += 1
print(cnt)