from re import *

with open('Task-24-6636-file.txt') as f:
    data = f.readline()

para = r'([24][135])+'
reg = rf'(?=({para}))'

m = [x.group(1) for x in finditer(reg, data)]

print(len(max(m, key=len)) // 2)