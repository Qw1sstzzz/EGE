# from fnmatch import *
#
# for x in range(290232310 - 290232310 % 1984, 10**10 + 1, 1984):
#     for ch1 in '2468':
#         for nech in '13579':
#             for ch2 in '02468':
#                 if fnmatch(str(x), f'{ch1}9?23?*23{nech}{ch2}'):
#                     print(x, x//1984)
# 2902302336 1462854
from itertools import *
ans = []
for r in range(3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for ch1 in '2468':
            for nech in '13579':
                for ch2 in '02468':
                    for v1 in '0123456789':
                        for v2 in '0123456789':
                            x = int(f'{ch1}9{v1}23{v2}{z}23{nech}{ch2}')
                            if x < 10**10 and x % 1984 == 0:
                                ans.append([x, x//1984])
ans = sorted(ans)

for i in ans:
    print(*i)