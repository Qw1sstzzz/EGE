from itertools import *
from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
alph = alph[:25]

cnt = 0
for val in product(alph, repeat=4):
    s = ''.join(val)
    if s[0] != '0':
        nech = len([int(i, 25) for i in s if int(i, 25) % 2 != 0])
        bigger_than_5 = len([int(i, 25) for i in s if int(i, 25) <= 5])
        if nech == 1 and bigger_than_5 <= 2:
            cnt += 1
print(cnt)

# 95700