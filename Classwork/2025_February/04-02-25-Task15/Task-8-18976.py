from itertools import *
from string import digits, ascii_uppercase


alph = (digits + ascii_uppercase)[:20]
ch = alph[::2]
nech = alph[1::2]
print(ch, nech)
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        summi = int(val[0], 20) + int(val[-1], 20)
        for i in ch:
            val = val.replace(i, '*')
        for i in nech:
            val = val.replace(i, '!')
        if summi == 26:
            if '*!*!*' == val or '!*!*!' == val:
                cnt += 1

print(cnt)