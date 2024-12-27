from itertools import *
graph = 'DE DB BE EA AH HC CF FG GH GB'.split()
matrix = '38 58 146 36 27 347 568 127'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print('')
print(6 + 31)