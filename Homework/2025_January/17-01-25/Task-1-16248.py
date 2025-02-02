from itertools import *

graph = 'BA BC AC AD CD CE ED DF FE EG FG'.split()
matrix = '347 3456 1245 1237 236 25 14'.split()

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) +1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        break

# 42