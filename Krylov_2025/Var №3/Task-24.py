from re import *

with open('24var03.txt') as f:
    data = f.readline().strip()

num = r'([1-9][0-9]*|0)'
reg = rf'(?:{num})((?:[-*])(?:{num}))+'

reg = rf'(?=({reg}))'

m = [x.group(1) for x in finditer(reg, data)]

print(len(max(m, key=len)))