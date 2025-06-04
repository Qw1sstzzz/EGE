with open('Task-24-19254-file.txt') as f:
    data = f.readline().strip()

m = 0
data = data.split('FSRQ')

for i in range(len(data) - 80):
    ps = 'SRQ' + 'FSRQ'.join(data[i:i+81]) + 'FSR'
    m = max(m, len(ps))

print(m)