from itertools import *

graph = 'AE AF FD DE DB BH EH HG BG GC CF'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print(14 + 17)