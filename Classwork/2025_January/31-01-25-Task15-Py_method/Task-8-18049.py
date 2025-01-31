from itertools import *

alph = sorted('012345678')

cnt = 0
for val in product(alph, repeat=7):
    s = ''.join(val)
    if s[0] not in '0246':
        r = s[-3:]
        if len(r) == len(set(r)):
            cnt += 1

print(cnt)

# 1837080