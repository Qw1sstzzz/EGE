with open('Task-24-19489-file.txt') as file:
    data = file.readline().strip()

while 'WSFWW' in data: data = data.replace('WSFWW', 'WSFW SFWW')
while 'WWF' in data: data = data.replace('WWF', '***')

data = data.split()
m = 0

for i in data:
    if len(i) > m:
        ans = []
        if i.count('***') <= 120:
            m = max(len(i), m)
        else:
            i = i.split('***')
            for k in range(len(i)):
                ps = '***'.join(i[k:k+121])
                m = max(len(ps), m)
print(m)
