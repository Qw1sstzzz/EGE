from re import *
with open('Task-24-19149-file.txt') as file:
    data = file.readline()

num = r'[1-4]*[24]'
reg = rf'[(]{num}([+]{num})+[)]'

x = [i.group() for i in finditer(reg, data)]
print(len(max(x, key=len)), max(x, key=len))