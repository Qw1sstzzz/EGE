from itertools import *

graph = 'AB BC AG AH HG GF HE EF ED DC CF'.split()
matrix = '568 36 247 368 178 124 35 145'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 4815