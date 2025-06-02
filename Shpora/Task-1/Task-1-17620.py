from itertools import *

graph = 'AF AB BF BD DE FE EC CG GD'.split()
matrix = '256 134 267 27 16 135 34'.split()

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        break

print(53 + 2)