with open('Task-24-4544-file.txt') as f:
    data = f.readline().strip()

while 'XIX' in data: data = data.replace('XIX', 'XI IX')
data = data.split()

print(len(max(data, key=len)))