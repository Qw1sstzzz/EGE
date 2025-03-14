with open('Task-24-19489-file.txt') as file:
    data = file.readline().strip()

data = data.replace('WSFWW', 'WSFW SFWW')

data = data.split()

m = 0

for i in data:
    if i.count('WWF') <= 120:
        m = max(len(i), m)

print(m)