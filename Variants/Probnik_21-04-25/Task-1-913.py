from itertools import *

graph = 'AE AC AB BD BF DF DC CE EG GF'.split()
matrix = '235 146 145 236 137 247 56'.split()

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)