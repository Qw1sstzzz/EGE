from itertools import *

ans = []
for r in range(6):
    for z in product('02468', repeat=r):
        z = ''.join(z)
        for v1 in '13579':
            for v2 in '13579':
                x = int(f'{z}12{v1}4{v2}')
                if x > 10**10:
                    quit()
                if x % 9231 == 0:
                    ans.append([x, x//9231])

ans = sorted(ans)

for i in ans[1:]:
    print(*i)