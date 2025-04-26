from re import *

with open('Task-24-332-file.txt') as f:
    data = f.readline()

sl1 = r'([ABC][abc]*)'
sl = r'([abcABC][abc]*)'
reg = rf'{sl1}([ ]{sl})*[.]'
reg = rf'(?=({reg}))'

m = finditer(reg, data)
ans = []

for i in m:
    s = i.group(1)
    ans.append([len(s), s])

print(max(ans))