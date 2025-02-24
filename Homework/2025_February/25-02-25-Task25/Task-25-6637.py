from fnmatch import fnmatch
from itertools import *

'''
for x in range(1021394 - 1021394 % 3052, 10**10+1, 3052):
    if fnmatch(str(x), '1?2139*4'):
        print(x, x//3052)
'''

ans = []

for r in range(4):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            x = int(f'1{v}2139{z}4')
            if x % 3052 == 0:
                ans.append([x, x//3052])

ans = sorted(ans)

for i in ans:
    print(*i)
