'''
from fnmatch import fnmatch

for x in range(2658, 10**9, 2658):
    if fnmatch(str(x), '85?16*4'):
        print(x, x//2658)

'''

from itertools import product, repeat

'1000000000'
'85___16?4'

ans = []
for r in range(4):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            num = int(f'85{v}16{z}4')
            if num % 2658 == 0:
                ans.append([num, num // 2658])

ans = sorted(ans)

for i in ans:
    print(*i)

# 85316484 32098
# 850169274 319853
# 851166024 320228
# 852162774 320603
# 854169564 321358
# 855166314 321733
# 856163064 322108
# 858169854 322863
# 859166604 323238
