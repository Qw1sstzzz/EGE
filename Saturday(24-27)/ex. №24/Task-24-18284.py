from re import *

with open('Task-24-18284-file.txt') as f:
    data = f.readline()

reg = r'L[^L]*?O.*?V.*?E'

m = [x.group() for x in finditer(reg, data)]

print(len(min(m, key=len)))