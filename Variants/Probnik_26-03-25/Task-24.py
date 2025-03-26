with open('Task-24-file.txt') as file:
    data = file.readline()
'''
from re import *

num = r'0|[2468]|[1-9]([0-9])*[02468]'

reg = rf'{num}([+*]{num})+'

m = max([x.group() for x in finditer(reg, data)],key=len)
print(len(m), m)
'''

def check(s):
    s = s.replace('*', ' ')
    s = s.split()
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True

data = data.replace('+', '*')
while '**' in data: data = data.replace('**', '* *')
m = 0

data = data.split()
ans = []
for i in data:
    s = i.strip('*')
    if m < len(s):
        if check(s):
            ans.append([len(s), s])
print(max(ans))
