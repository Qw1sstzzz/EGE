from re import *

with open('24var02.txt') as f:
    data = f.readline().strip()

num = r'[5-8][0-8]*|0'
reg = rf'(?:[+])(?:{num})((?:[-+])(?:{num}))+'

m = [x.group() for x in finditer(reg, data)]

print(len(max(m, key=len)))