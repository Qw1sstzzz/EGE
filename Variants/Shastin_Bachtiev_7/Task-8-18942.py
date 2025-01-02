from itertools import *

alph = set('ДИОНИСИЙ')
cnt = 0

for s in product(alph, repeat=6):
    s = ''.join(s)
    if (s.count('Д') >= 1 and s.count('Н') == 0) or (s.count('Н') >= 1 and s.count('Д') == 0):
        if all(s[i] != s[i+1] for i in range(len(s) - 1)):
            cnt += 1
print(cnt)
# 8296