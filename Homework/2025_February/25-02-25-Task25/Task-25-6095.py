from fnmatch import fnmatch
from itertools import *

'''

for x in range(157424, 10**8+1):
    if fnmatch(str(x), '*15*7424'):
        if (x % 111 == 0) and (x % 113 != 0) and (x % 127 != 0):
            print(x, x//111)
        elif (x % 111 != 0) and (x % 113 == 0) and (x % 127 != 0):
            print(x, x//113)
        elif (x % 111 != 0) and (x % 113 != 0) and (x % 127 == 0):
            print(x, x//127)
# Не досчитало
'''



ans = []
for r1 in range(2):
    for r2 in range(2):
        for z1 in product('0123456789', repeat=r1):
            for z2 in product('0123456789', repeat=r2):
                z1 = ''.join(z1)
                z2 = ''.join(z2)
                
                x = int(f'{z1}15{z2}7424')
                
                if x > 10**8:
                    quit()
                else:
                    if (x % 111 == 0) and (x % 113 != 0) and (x % 127 != 0):
                        ans.append([x, x//111])
                    elif (x % 111 != 0) and (x % 113 == 0) and (x % 127 != 0):
                        ans.append([x, x//113])
                    elif (x % 111 != 0) and (x % 113 != 0) and (x % 127 == 0):
                        ans.append([x, x//127])

ans = sorted(ans)

for i in ans:
    print(*i)
