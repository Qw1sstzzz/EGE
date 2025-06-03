from itertools import *

alph = sorted('ПОБЕДА')
ans = []

for pos, val in enumerate(product(alph, repeat=6), start=1):
    s = ''.join(val)
    if pos % 2 == 0 and s[0] == 'О' and len(set(s)) == len(s):
        ans.append([pos, s])
print(max(ans))