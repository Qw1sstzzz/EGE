with open('Task-24-20909-file.txt') as f:
    data = f.readline().strip()

m = 0
data = data.split('AB')

for i in range(len(data) - 100):
    ps = 'B' + 'AB'.join(data[i:i+101]) + 'A'
    m = max(m, len(ps))

print(m)
