from re import *

with open('Task-24-8579-file.txt') as f:
    data = f.readline().strip()

reg = r'([02468][A-Z]+[13579])|([13579][A-Z]+[02468])'
reg = rf'(?=({reg}))'

m = [i.group(1) for i in finditer(reg, data)]

print(len(max(m, key=len)))