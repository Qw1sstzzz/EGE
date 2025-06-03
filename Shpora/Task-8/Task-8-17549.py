from itertools import *

alph = sorted('ФОКУС')
ans = []

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('Ф') == 0 and val.count('У') == 2:
        ans.append([pos, val])

print(max(ans))