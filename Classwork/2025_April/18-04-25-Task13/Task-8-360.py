from itertools import *
alph = sorted('ИНСТАВК')
sogl = sorted('НСТВК')
gl = sorted('ИА')
cnt = 1
ans = []
for k1 in sogl:
    for k2 in alph:
        for k3 in alph:
            for k4 in gl:
                s = k1 + k2 + k3 + k4
                if s == 'НИКА':
                    ans.append([cnt, s])
                if s == 'ВААА':
                    ans.append([cnt, s])
                cnt += 1
print(ans)
