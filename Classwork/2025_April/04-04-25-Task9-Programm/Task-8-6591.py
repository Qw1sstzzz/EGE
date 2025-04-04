from itertools import *

alph = '0123456'
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        summ_ch = sum([int(i) for i in val if int(i) % 2 == 0])
        summ_nech = sum([int(i) for i in val if int(i) % 2 != 0])
        if summ_ch < summ_nech:
            cnt += 1
print(cnt)