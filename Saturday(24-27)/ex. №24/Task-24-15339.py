from re import *

with open('Task-24-15339-file.txt') as file:
    data = file.readline()

reg = r'[A-C]([6-9][A-C])+[6-9]?|[6-9]([A-C][6-9])+[A-C]?'

m = [x.group() for x in finditer(reg, data)]

print(len(max(m, key=len)))