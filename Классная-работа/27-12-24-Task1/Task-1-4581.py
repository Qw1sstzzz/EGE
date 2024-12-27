from itertools import permutations

graph = 'AB AD AF DE EG GC CF FB BE'.split() # Выписывем каждое ребро
matrix = '37 367 125 56 34 247 126'.split() # Выписываем таблицу (Матрицу)

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
