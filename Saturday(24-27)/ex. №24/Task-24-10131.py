from string import ascii_uppercase

with open('Task-24-10131-file.txt') as file:
    data = file.readline().strip()

for c in ascii_uppercase[2:]:
    data = data.replace(c, '*')

m = 0
for i in range(len(data) - 1):
    ps = data[i]
    for j in range(i+1, len(data)):
        ps += data[j]
    if len(ps) > 10_000:
        if ps.count('A') == ps.count('B'):
            m = max(len(ps), m)

print(m)