with open('Task-24-17535-file.txt') as f:
    data = f.readline().strip()

data = data.split('CD')
m = 0

for i in range(len(data) - 160):
    s = 'D' + 'CD'.join(data[i:i+161]) + 'C'
    m = max(m, len(s))

print(m)
