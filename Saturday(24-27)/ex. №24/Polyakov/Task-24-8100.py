from re import *

with open('Task-24-335-file.txt') as f:
    data = f.readline()

num1 = r'[1-9][0-9]*[12346789]|[1-9]'
num2 = r'[1-9][0-9]*[05]|[05]'

express = rf'\(({num1})[-+]({num2})\)'
reg = rf'({express})+'
m = finditer(reg, data)
ans = []

for i in m:
    n = i.group()
    ans.append(len(n))

print(max(ans))