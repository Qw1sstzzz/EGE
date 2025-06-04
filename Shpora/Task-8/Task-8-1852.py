from itertools import *

alph = 'ГЕПАРД'
cnt = 0

for i in product(alph, repeat=5):
    s = ''.join(i)
    if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
        cnt += 1
print(cnt)