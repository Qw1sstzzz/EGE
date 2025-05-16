from re import *

with open('Task-24-15339-file.txt') as f:
    data = f.readline()

reg = r'([ABC][6789])+[ABC]?|([6789][ABC])+[6789]?'

reg = rf'(?=({reg}))'

m = [x.group(1) for x in finditer(reg, data)]

print(len(max(m, key=len)))