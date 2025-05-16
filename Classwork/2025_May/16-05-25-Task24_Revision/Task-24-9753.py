with open('Task-24-9753-file.txt') as f:
    data = f.readline().strip()

data = data.split('Y')
m = 0

for i in range(len(data) - 150):
    s = 'Y'.join(data[i:i+151])
    m = max(m, len(s))

print(m)