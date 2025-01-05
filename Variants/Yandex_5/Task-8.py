from itertools import *

cnt = 0

for val in product(sorted('КЗБС'), repeat=5):
    val = ''.join(val)
    if val.count('З') <= 2 and 'КБ' not in val and 'БК' not in val:
        cnt += 1
print(cnt)