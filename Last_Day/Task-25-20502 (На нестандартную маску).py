from itertools import *

ans = []
for r in range(5):
    for resh in product('02468', repeat=r):
        resh = ''.join(resh)
        for s1 in '13579':
            for s2 in '13579':
                num = int(f'20{s1}{s2}22{resh}')
                if num % 10980 == 0:
                    ans.append([num, num // 10980])

ans = sorted(ans)
cnt = 0
for i in ans:
    print(*i)
    cnt += 1
    if cnt == 5:
        break