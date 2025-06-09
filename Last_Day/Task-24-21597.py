from re import *

with open('Task-24-21597-file.txt') as f:
    data = f.readline().strip()

num = r'([1-5][0-5]*|0)'

reg = rf'{num}([*]{num})+([-]{num})+'

reg = rf'(?=({reg}))' # Есть пересечение
matches = [x.group(1) for x in finditer(reg, data)]

print(len(max(matches, key=len)))