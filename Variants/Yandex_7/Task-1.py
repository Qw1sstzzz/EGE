from itertools import *

graph = 'KR KP RT TP TL TC RC PL CL LM MC'.split()
matrix = '235 14 1456 236 1367 3457 56'.split()

print(*range(1, 8))

for i in permutations('KPRTLCM'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)