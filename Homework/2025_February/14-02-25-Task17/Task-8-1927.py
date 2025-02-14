from itertools import *

alph = set(sorted('ЯСНОВИДЕЦ'))
gl = 'ЯОИЕ'
cnt = 0

for val in product(alph, repeat=5):
    s = ''.join(val)
    if (s[0] not in gl) and (s[-1] in gl):
        count_first = s.count(s[0])
        count_last = s.count(s[-1])
        if (count_first == 1) and (count_last == 1):
            cnt += 1
print(cnt)