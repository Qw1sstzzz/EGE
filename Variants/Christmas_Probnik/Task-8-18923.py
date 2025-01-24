from itertools import *

alph = sorted('ВЬЮГА')
cnt = 0

for val in product(alph, repeat=6):
    val = ''.join(val)
    if 'ЮГ' in val:
        cnt += 1
print(cnt)