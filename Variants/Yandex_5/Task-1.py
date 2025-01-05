from itertools import *

graph = 'LK LR LA LP PQ QA AC QC PB BC CR BK KR'.split()
matrix = '3457 456 167 128 126 2358 138 467'.split()

print(*range(1, 9))

for i in permutations('ABCKPQRL'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        break

# 27