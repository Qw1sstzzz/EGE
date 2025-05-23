from re import *

with open('Task-24-21597-file.txt') as f:
    data = f.readline()

num = r'([1-5][0-5]*|0)'
m = 0
reg = rf'{num}([*]{num})*([-]{num})*'
reg = rf'(?=({reg}))'
match = [x.group(1) for x in finditer(reg,data)]

for i in match:
    m = max(len(i), m)
print(m)