with open('Task-24-1975-file.txt') as f:
    data = f.readline()

while 'PP' in data: data = data.replace('PP', 'P P')
data = data.split()

print(len(max(data, key=len)))