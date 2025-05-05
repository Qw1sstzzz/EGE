from itertools import *

alph = '012345678'
cnt = 0

for i in product(alph, repeat=7):
    s = ''.join(i)
    if s[0] not in '01357':
        if int(s[-1]) % 3 != 0:
            if s.count('6') >= 1:
                cnt += 1
print(cnt)