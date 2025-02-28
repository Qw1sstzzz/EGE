from itertools import *

alph = sorted('КОТБУС')
cnt = 0

for val in product(alph, repeat=8):
    s = ''.join(val)
    if 'КОТ' in s and s[0] not in 'ОУ':
        cnt += 1
print(cnt)