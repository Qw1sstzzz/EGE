from re import *

with open('Task-24-6029-file.txt') as f:
    data = f.readline()

reg = r'(EF)+[E]?|(FE)+[F]?'
reg = rf'(?=({reg}))'

m = [x.group(1) for x in finditer(reg, data)]

print(len(max(m, key=len)))