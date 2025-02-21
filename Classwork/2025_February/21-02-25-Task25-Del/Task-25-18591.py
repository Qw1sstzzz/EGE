from itertools import *

'10000000000'
'C9?23?23NC'

chet = '02468'
nechet = '13579'
ans = []


for v1 in '0123456789':
    for C1 in chet:
        for v2 in '0123456789':
            for N in nechet:
                for C2 in chet:
                    num = int(f'{C1}9{v1}23{v2}23{N}{C2}')
                    if (num % 1984 == 0) and (num <= 10**10):
                        ans.append([num, num//1984])
ans  = sorted(ans)

for i in ans:
    print(*i)