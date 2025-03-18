from re import *

with open('Task-24-20813-file.txt') as file:
    data = file.readline().strip()
'''
num = r'[7-9][0-9]*'

reg = rf'{num}([-*]{num})+'

m = max([x.group() for x in finditer(reg, data)], key=len)

print(len(m), m)
'''

m = 0
data = data.replace('-', '*')
while '**' in data: data = data.replace('**', '* *')
for c in '89':
    data = data.replace(c, '7')
for c in range(2, 50):
    data = data.replace(f' {'0' * c}', ' 0')
for v in range(2, 50):
    data = data.replace(f' {'0' * c} ', ' 0 ')
for v in range(2, 50):
    data = data.replace(f'*{'0' * c}', '*0 0')
for v in range(2, 50):
    data = data.replace(f'*{'0' * c}*', '*0 0*')

data = data.split()
for i in data:
    if len(i) > m:
        if i.count('*') >= 1:
            m = max(len(i), m)
print(m)

