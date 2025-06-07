from itertools import *

graph = 'АВ АГ ГВ ВЕ ЕГ ЕЖ ЖИ ИГ ГД ДИ БД БГ'.split()
matrix = '26 134678 27 257 48 128 234 256'.split()

print(*range(1, 9))

for i in permutations('АБВГДЕЖИ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        break
print('Б Г А Е Ж Д В И')
print(20 + 11)