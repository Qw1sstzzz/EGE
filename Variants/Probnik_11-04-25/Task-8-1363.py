from itertools import *

alph = '01234'
cnt = set()

for val in product(alph, repeat=6):
    s = ''.join(val)
    if s[0] == '3':
        if s[-1] in '024':
            cnt.add(s)
print(len(cnt))