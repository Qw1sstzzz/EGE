with open('Task-24-18937-file.txt') as file:
    data = file.readline().strip()

m = 0

data = data.replace('*', '+')
while '++' in data: data = data.replace('++', '+ +')
for c in '345': data = data.replace(c, '2')

for n in range(1, 20):
    data = data.replace(f' {'0'*n}2', ' 2')
for n in range(1, 20):
    data = data.replace(f'+{'0'*n}2', '+0 2')
for n in range(2, 20):
    data = data.replace(f'+{'0'*n}+', '+0 0+')

data = data.split()
for i in data:
    i = i.strip('+')
    if len(i) > m and i.count('+') > 0:
        m = max(m, len(i))

print(m)


