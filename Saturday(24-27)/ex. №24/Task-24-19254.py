with open('Task-24-19254-file.txt') as file:
    data = file.readline().strip()
m = 0
data = data.replace('FSRQ', '****')

data = data.split('****')

for i in range(len(data) - 80):
    s = '****'.join(data[i:i+81])
    s = '***' + s + '***'
    m = max(len(s), m)

print(m)