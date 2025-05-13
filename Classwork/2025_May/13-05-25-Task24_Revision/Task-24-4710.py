from re import *

with open('Task-24-4710-file.txt') as f:
    data = f.readline()

para = r'([CDF][AO])+'
reg = rf'(?=({para}))'

m = [x.group(1) for x in finditer(reg, data)]

print(len(max(m, key=len)) // 2)