from itertools import *

alph = '01234567'
cnt = 0

for i in product(alph, repeat=5):
    s = ''.join(i)
    if s[0] not in '01357' and s[-1] not in '26':
        if s.count('7') <= 2:
            cnt += 1
print(cnt)