with open('Task-24-21717-file.txt') as f:
    data = f.readline().strip()

m = 1_000_000_000

data = data.split('RSQ')

for i in range(len(data) - 130):
    ps = 'RSQ'.join(data[i:i+131]) + '*'
    m = min(m, len(ps))
print(m)