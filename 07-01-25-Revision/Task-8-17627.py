from itertools import *
from string import digits, ascii_uppercase

alph = '0123456789*****'
ans = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('8') == 1 and val[0] != '0' and val.count('*') >= 2:
        ans += 1
print(ans)

# 83175