from itertools import *

alph = sorted('ДГИАШЭ')
ans = set()

for i in product(alph, repeat=5):
    i = ''.join(i)
    if i[0] not in 'ИАЭ' or i[-1] in 'ИАЭ':
        ans.add(i)
print(len(ans))

# 1944