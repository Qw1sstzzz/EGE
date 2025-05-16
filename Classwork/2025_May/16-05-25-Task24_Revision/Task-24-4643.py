with open('Task-24-4643-file.txt') as f:
    data = f.readline().strip()

data = data.replace('2', '1')
data = data.replace('B', 'A')
data = data.replace('11A', '*')
data = data.replace('A', ' ')
data = data.replace('1', ' ')

print(len(max(data.split(), key=len)))