from itertools import *

graph = 'DE EF EH HG GF FC HA GA AB BC CD'.split()
matrix = '568 36 247 368 178 124 35 145'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print('')
print('64815')