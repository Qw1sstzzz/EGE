with open('Task-24-4643-file.txt') as file:
    data = file.readline().strip()

data = data.replace('B', 'A')
data = data.replace('2', '1')

while '11A' in data:
    data = data.replace('11A', '***')

data = data.replace('A', ' ').replace('1', ' ')
data = data.split()
m = 0
for i in data:
    if m < len(i) // 3:
        m = max(m, len(i) // 3)

print(m)