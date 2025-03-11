from re import *

with open('Task-24-19968-file.txt') as file:
    data = file.readline().strip()

num = r'([1-5][0-5]*|0)'

reg = rf'{num}([+*]{num})*'

m = max([x.group() for x in finditer(reg, data)], key=len)

print(len(m), m)