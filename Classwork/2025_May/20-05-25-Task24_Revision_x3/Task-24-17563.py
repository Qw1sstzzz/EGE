from re import *

with open('Task-24-17563-file.txt') as f:
    data = f.readline()

num = r'([7-9][0-9]*)'

reg = rf'(?:{num})([-*]{num})+'
reg = rf'(?=({reg}))'
matches = [x.group(1) for x in finditer(reg, data)]

print(len(max(matches, key=len)))