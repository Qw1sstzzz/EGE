from itertools import *

graph = 'АБ БД ДА АГ ГД ГВ ДЕ ЕЗ ЗВ ЗЖ ЖВ'.split()
matrix = '245 15 478 135 1246 58 38 367'.split()

print(*range(1, 9))

for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print('Г - В - З', 10 + 2)
print('Г - В - Ж - З', 10 + 2 + 2)
print('Г - Д - Е - З', 9 + 1 + 2)
print('Г - А - Д - Е - З', 5 + 4 + 1 + 2)
print('Г - А - Б - Д - Е - З', 5 + 1 + 2 + 1 + 2)