from itertools import *

def qub(num):
    return sum(map(int, num))**3

ans = []
for r in range(7):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        x = int('1234' + z)
        if (x % 137 == 0) and (int(z) % qub(z) == 0):
            ans.append(x)

ans = sorted(ans)

for i in ans:
    print(i)
