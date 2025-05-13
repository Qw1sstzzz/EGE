with open('Task-24-4682-file.txt') as f:
    data = f.readline()

for c in 'BCD':
    data = data.replace(c, '0')
for c in 'AE':
    data = data.replace(c, '1')

while '10' in data: data = data.replace('10', '*')
data = data.replace('1', ' ').replace('0', ' ')

print(len(max(data.split(), key=len)))
