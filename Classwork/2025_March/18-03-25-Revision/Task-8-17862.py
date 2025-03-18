from itertools import *

alph= '0123456789AB'
cnt = 0

for i in product(alph, repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('7') == 1:
            kol_vo = len([i for i in s if int(i, 12) > 8])
            if kol_vo <= 3:
                cnt += 1
print(cnt)