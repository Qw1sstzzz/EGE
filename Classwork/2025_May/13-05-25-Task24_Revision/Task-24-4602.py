from re import *

with open('Task-24-4602-file.txt') as f:
    data = f.readline()

para = r'([BCD][AO])+'
para = rf'(?=({para}))'

m = [x.group(1) for x in finditer(para, data)]
print(len(max(m, key=len)) // 2)