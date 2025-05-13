from re import *

with open('Task-24-6054-file.txt') as f:
    data = f.readline()

para = r'([BC][BC][A])+'
reg = rf'(?=({para}))'

m = [x.group(1) for x in finditer(reg, data)]

print(len(max(m, key=len)))