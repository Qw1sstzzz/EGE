from itertools import *

cnt = 0
alph = '0123456789AB'

for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('B') == 2:
            for c in '02468A':
                val = val.replace(c, '*')
            for x in '13579B':
                val = val.replace(x, '!')

            if val == '*!*!*!*' or val == '!*!*!*!':
                cnt += 1

print(cnt)

# 48600