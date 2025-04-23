with open('Task-24-21717-file.txt') as f:
    data = f.readline()

data = data.split('RSQ')
m = 1_000_000_000

for i in range(len(data) - 130):
    s = 'RSQ'.join(data[i:i+131]) + '*'
    m = min(m, len(s))

print(m)