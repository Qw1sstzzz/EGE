from re import *

with open('24var01.txt') as f:
    data = f.readline().strip()

num = r'0|[1-4][0-4]*'
reg = rf'(?:{num})((?:[+-])(?:{num}))+'
# 01-220... -> Благодаря ?: 1-220...

m = [x.group() for x in finditer(reg, data)]

print(len(max(m, key=len)), max(m, key=len))

