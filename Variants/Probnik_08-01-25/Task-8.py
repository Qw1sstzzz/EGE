from itertools import *

alph = sorted('ABCDEF')
gl = 'AE'
cnt = 0

for i in product(alph, repeat=6):
    i = ''.join(i)
    if (i[0] not in gl) and (i[-1] not in gl):
        cnt += 1
print(cnt)

# 20736
