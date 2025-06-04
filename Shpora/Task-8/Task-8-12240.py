from itertools import *

alph = '012345678'
cnt = 0
for i in product(alph, repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('5') == 1:
        for j in range(len(s) - 1):
            if s[j] == s[j+1]:
                break
        else:
            cnt += 1
print(cnt)