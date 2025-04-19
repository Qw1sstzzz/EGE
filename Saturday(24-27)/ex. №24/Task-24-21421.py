from re import *

with open('Task-24-21421-file.txt') as f:
    data = f.readline()

num = r'[1-9AB][0-9AB]*[02468A]'

m = [x.group() for x in finditer(num, data)]
print(len(max(m, key=len)))