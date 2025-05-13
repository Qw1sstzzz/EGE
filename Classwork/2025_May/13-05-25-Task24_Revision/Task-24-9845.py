with open('Task-24-9845-file.txt') as f:
    data = f.readline()

for c in 'ABC':
    data = data.replace(c, '*')

for c in '89':
    data = data.replace(c, '!')

while '!!' in data: data = data.replace('!!', '! !')
while '**' in data: data = data.replace('**', '* *')

print(len(max(data.split(), key=len)))