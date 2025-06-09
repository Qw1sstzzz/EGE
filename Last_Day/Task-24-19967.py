from re import *

with open('Task-24-19967-file.txt') as f:
    data = f.readline().strip()

num = r'([1-9A-F][0-9A-F]*|0)'

reg = rf'AFD{num}([+*]{num})+'
reg = rf'(?=({reg}))'

matches = [x.group(1) for x in finditer(reg, data)]

print(len(max(matches, key=len)))
print(max(matches, key=len))