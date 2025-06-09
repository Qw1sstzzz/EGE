from re import *

with open('Task-24-19751-file.txt') as f:
    data = f.readline().strip()

num = r'[1-9][0-9]*'
reg = rf'A{num}([+]{num})*'

# reg = rf'(?=({reg}))'

matches = [x.group() for x in finditer(reg, data)]

ans = []
for i in matches:
    i = i[1:]
    ans.append(eval(i))

print(max(ans))