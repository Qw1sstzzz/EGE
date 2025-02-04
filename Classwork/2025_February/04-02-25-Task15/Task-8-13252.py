from itertools import *

ans = set()
alph = 'КИДАЛА'

for val in permutations(alph, r=5):
    val = ''.join(val)

    if 'АА' not in val:
        ans.add(val)

print(len(ans))