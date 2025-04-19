from re import *

with open('Task-24-18597-file.txt') as f:
    data = f.readline()

num = r'[1-9][0-9]{3}[.][0-9]+'
reg = rf'{num}[&]{num}'

match = [x.group() for x in finditer(reg,data)]
print(len(max(match, key=len)))