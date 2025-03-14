from re import *

with open('Task-24-18937-file.txt') as file:
    data = file.readline()

num = r'[1-9][0-9]*'

reg = rf'{num}([+*]{num})+'

m = max([x.group() for x in finditer(reg, data)], key=len)

print(len(m))