with open('Task-24-16269-file.txt') as file:
    data = file.readline()

for c in 'TUVW':
    data = data.replace(c, ' ')

while 'XXX' in data: data = data.replace('XXX', 'XX XX')
while 'YYY' in data: data = data.replace('YYY', 'YY YY')
while 'ZZZ' in data: data = data.replace('ZZZ', 'ZZ ZZ')

print(len(max(data.split(), key=len)))