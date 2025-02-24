from itertools import *

ans = []
for r in range(7):
    for z in product('13579', repeat=r):
        z = ''.join(z)
        for v in '2468':
            x = int(f'{v}136{z}')
            if x % 53191 == 0:
                ans.append([x, x//53191])

ans = sorted(ans)

for i in ans[-5:]:
    print(*i)
