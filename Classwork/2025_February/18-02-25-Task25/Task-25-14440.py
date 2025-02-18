from fnmatch import fnmatch
from itertools import product

def prime(num):
    for x in range(2, int(num * 0.5) + 1):
        if num % x == 0:
            return False
    return True

def multiply(num):
    r = 1
    for i in str(num):
        r *= int(i)
    return r

'''
for x in range(315670, 10**7):
    if fnmatch(str(x), '31*567?') and prime(x):
        print(x, multiply(x))
'''

res = []

for r in range(2):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            num = int(f'31{z}567{v}')
            if prime(num):
                res.append([num, multiply(num)])

res = sorted(res)

for i in res:
    print(*i)