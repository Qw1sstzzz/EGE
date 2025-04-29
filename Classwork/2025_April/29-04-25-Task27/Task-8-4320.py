from itertools import *

alph = '01234567'
cnt = 0

for i in product(alph, repeat=6):
    s = ''.join(i)
    if s[0] != '0':
        if len(set(s)) == len(s):
            if int(s, 8) % 5 == 0:
                for c in '0246': s = s.replace(c, '*')
                for c in '1357': s = s.replace(c, '!')
                if '**' not in s and '!!' not in s:
                    cnt += 1
print(cnt)