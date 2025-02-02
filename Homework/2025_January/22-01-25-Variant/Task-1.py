from itertools import *

graph = 'AG GF FB BD DE EA EC CG CB'.split()
matrix = '47 57 45 136 236 457 126'.split()

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        break

# CB CG CE
# 13 11 17
# 41