from itertools import *

alph = 'ПАРИЖАНКА'
cnt = 0
for i in set(permutations(alph)):
    s = ''.join(i).replace('И', 'А')
    if s.count('АА') == 1 and 'ААА' not in s:
        cnt += 1
print(cnt)