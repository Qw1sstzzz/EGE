from itertools import *
cnt = 0
alph = '012345678'

for val in product(alph, repeat=7):
    s = ''.join(val)
    if s[0] != '0' and s[-1] not in '347':
        for i in range(len(s) - 2):
            if s[i] == s[i+1] and s[i+1] == s[i+2]:
                break
        else:
            cnt += 1
print(cnt)