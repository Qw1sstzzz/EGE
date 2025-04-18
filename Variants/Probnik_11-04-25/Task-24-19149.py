from re import *
with open('Task-24-19149-file.txt') as file:
    data = file.readline()

num = r'[1-4][1-4]*'
reg = rf'[(]{num}([+]{num})+[)]'
m = 0
x = [i.group() for i in finditer(reg, data)]
for i in x:
    if eval(i) % 2 == 0:
        m = max(len(i), m)

print(m)