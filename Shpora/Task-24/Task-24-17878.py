from re import *

with open('Task-24-17878-file.txt') as f:
    data = f.readline().strip()

num = r'([6-9][0-9]*|0)'
reg = rf'{num}([-*]{num})+'

reg = rf'(?=({reg}))'

m = [x.group(1) for x in finditer(reg, data)]

print(len(max(m, key=len)))

