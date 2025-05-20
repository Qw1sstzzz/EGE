from re import *

with open('Task-24-17641-file.txt') as f:
    data = f.readline().strip()

num = r'([1-9][0-9]*|0)'
reg = rf'{num}([+*]{num})+'

matches = [x.group() for x in finditer(reg, data)]
m = 0
for i in matches:
    if eval(i) == 0:
        m = max(m, len(i))
    else:
        for l in range(len(i) + 1):
            for r in range(len(i), l, -1):
                sub_str = i[l:r].strip('*+')
                if len(sub_str) >= 2:
                    if sub_str[0] == '0' and sub_str[1] in '0123456789':
                        continue
                    if eval(sub_str) == 0:
                        m = max(m, len(sub_str))
                        break
print(m)

