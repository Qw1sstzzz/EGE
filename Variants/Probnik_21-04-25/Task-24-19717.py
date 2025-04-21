with open('Task-24-19717-file.txt') as f:
    data = f.readline()
data = data.split('M')
m = 0
for i in range(len(data) - 278):
    s = 'M'.join(data[i:i+279])
    m = max(m, len(s))
print(m)