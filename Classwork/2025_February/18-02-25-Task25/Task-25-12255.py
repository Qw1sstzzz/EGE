
from fnmatch import fnmatch

for x in range(1203456009 - 1203456009 % 98591, 10**12+1, 98591):
    if fnmatch(str(x), '12?3*456??9'):
        print(x, x // 98591)

'''
from itertools import product

res = []


for z in product('0123456789', repeat=1):
    s = ''.join(z)
    for v in '0123456789':
        num = int(f'12 + {v} + 3 + {z} + 456 + {v} + {v} + 9')
        if num % 98591 == 0 and num < 10**12+1:
            res.append([num, num//98591])

res = sorted(res)
for i in res:
    print(*i)
'''