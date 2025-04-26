from re import *

with open('Task-24-333-file.txt') as f:
    data = f.readline()
# data = 'alex@@s..ch@gmail.com.runet@yandex.rubo@yandex.ru'

name = r'([a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*)'
y = 'yandex.ru'
g = 'gmail.com'

posled1 = rf'({y})*(({g})*({y}))*'
posled2 = rf'({g})*(({y})*({g}))*'

server = rf'({posled1})|({posled2})'

reg = rf'({server})*({name})[@]({server})'
reg = rf'(?=({reg}))'

m = finditer(reg, data)
ans = []

for i in m:
    s = i.group(1)
    ans.append(len(s))

print(max(ans))