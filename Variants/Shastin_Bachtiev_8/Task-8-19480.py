from itertools import *

alph = 'ПАРИЖАНКА'
ans = set()
for i in permutations(alph):
    s = ''.join(i)
    if s.count('АА') == 1:
        ans.add(s)
print(len(ans))