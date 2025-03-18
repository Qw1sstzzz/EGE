from re import *

with open('Task-24-20813-file.txt') as file:
    data = file.readline().strip()

num = r'[7-9][0-9]*'

reg = rf'{num}([-*]{num})+'

m = max([x.group() for x in finditer(reg, data)], key=len)

print(len(m), m)