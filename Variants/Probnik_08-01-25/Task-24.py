with open('Task-24-11636-file.txt') as file:
    data = file.readline().strip()

A_first = data.find('A')
A_last = data.rfind('A')
data = data[A_first:A_last+1]

t = []
for i in range(len(data) - 2):
    ps = data[i]
    for j in range(i+1, len(data) - 1):
        ps += data[j]
        if ps[-1] == 'A':
            break
    t.append(ps)
    ps = ''
res = []
for l in t:
    if l.count('A') != 1 and len(l) != l.count('A'):
        res.append(l)
print(len(res))



