from itertools import *

ans = set()
alph = sorted('ПАРИЖАНКА')

for val in permutations(alph):
    s = ''.join(val)
    s = s.replace('А', '*').replace('И', '!')
    cnt = [1 for i in range(len(s) - 1) if s[i] in '*!' and s[i+1] in '*!']
    if len(cnt) == 1:
        ans.add(s)
print(len(ans))