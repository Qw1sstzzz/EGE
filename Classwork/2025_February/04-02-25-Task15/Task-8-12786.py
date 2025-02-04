from itertools import *

ans = set()
alph = 'МАКАКА'

for val in permutations(alph):
    val = ''.join(val)
    val = val.replace('А', '*')
    val = val.replace('К', '!')
    if '**' not in val and '!!' not in val:
        ans.add(val)

print(len(ans))