from itertools import *

'10000000000'
'1A2157___4'
chet = '02468'
nechet = '13579'

ans = []

for r in range(4):
    for B in product(nechet, repeat=r):
        B = ''.join(B)
        for A in chet:
            num = int(f'1{A}2157{B}4')
            if num % 133 == 0:
                ans.append([num, num//133])

ans = sorted(ans)

for i in ans:
    print(*i)