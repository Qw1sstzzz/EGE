with open('Task-24-4682-file.txt') as file:
    data = file.readline().strip()

data = data.replace('E', 'A')
for c in 'CD':
    data = data.replace(c, 'B')

while 'AA' in data: data = data.replace('AA', ' A')
while 'BB' in data: data = data.replace('BB', 'B ')

data = data.split()

print(len(max(data, key=len))//2)