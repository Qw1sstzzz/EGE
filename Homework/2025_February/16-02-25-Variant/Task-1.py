from itertools import *

graph = 'АБ БГ АГ АВ ВГ ГЕ ЕЗ ГЗ ЗЖ ГЖ ЖД ГД'.split()
matrix = '235 13 1245678 36 13 347 368 37'.split()

print(*range(1, 9))

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        break

print(16 + 17 + 11)