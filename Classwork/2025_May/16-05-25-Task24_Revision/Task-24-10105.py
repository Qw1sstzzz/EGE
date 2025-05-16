with open('Task-24-10105-file.txt') as f:
    data = f.readline().strip()

data = data.split('T')
m = 0

for i in range(len(data) - 100):
    s = 'T'.join(data[i:i+101])
    m = max(m, len(s))

print(m)
