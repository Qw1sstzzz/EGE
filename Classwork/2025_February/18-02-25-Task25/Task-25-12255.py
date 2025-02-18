'''
from fnmatch import fnmatch

for x in range(1203456009 - 1203456009 % 98591, 10**12+1, 98591):
    if fnmatch(str(x), '12?3*456??9'):
        print(x, x // 98591)
'''
from itertools import product

res = []
# '1000000000000'
# '12?3__456??9'
for r in range(3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v1 in '0123456789':
            for v2 in '0123456789':
                for v3 in '0123456789':
                    num = int(f'12{v1}3{z}456{v2}{v3}9')
                    if (num % 98591 == 0) and (num < 10**12+1):
                        res.append([num, num//98591])

    res = sorted(res)
    for i in res:
        print(*i)
