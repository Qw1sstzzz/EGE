from re import *

with open('Task-24-21597-file.txt') as f:
    data = f.readline()

num = r'([1-5][1-5]*)'

reg = rf'[({num}\*)]+'
match = [x.group() for x in finditer(reg,data)]
for i in match:
    print(i)
    input()