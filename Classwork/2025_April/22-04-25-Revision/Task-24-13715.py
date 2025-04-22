with open('Task-24-13715-file.txt') as f:
    data = f.readline()

m = 0
data = data.split('AB')

for i in range(len(data) - 50):
    s = 'B' + 'AB'.join(data[i:i+51]) + 'A'
    m = max(m, len(s))
print(m)