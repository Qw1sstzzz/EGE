from itertools import *

gl = 'ИУ'
alph = sorted('МИНУС')
res = []

for pos, val in enumerate(product(alph, repeat=4) , start=1):
    val = ''.join(val)
    count_sgl = len([i for i in val if i not in gl])
    count_gl = len([i for i in val if i in gl])
    if count_sgl >= count_gl:
        res.append([pos, val])

print(max(res))
