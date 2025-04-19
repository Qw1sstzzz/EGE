from re import *

with open('Task-24-18147-file.txt') as f:
    data = f.readline()

reg = r'[7-9]+([+][7-9]+)+'

m = [x.group() for x in finditer(reg, data)]
ans = []

for i in m:
    ans.append(eval(i))

print(max(ans))