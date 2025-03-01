from itertools import permutations

graph = 'DE DB EB EA AH HC CF FG HG GB'.split()
matrix = '38 58 146 36 27 347 568 127'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)