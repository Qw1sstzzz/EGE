from itertools import *

alph = '0123456789ABCDE'
cnt = 0
for i in product(alph, repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('8') == 1:
        cnt_bol_9 = len([i for i in s if i not in '0123456789'])
        if cnt_bol_9 >= 2:
            cnt += 1
print(cnt)