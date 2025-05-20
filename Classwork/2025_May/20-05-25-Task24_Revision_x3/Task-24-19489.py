with open('Task-24-19489-file.txt') as f:
    data = f.readline().strip()

while 'WSFWW' in data: data = data.replace('WSFWW', 'WSFW SFWW')

data = data.split()
maxi = 0
for i in data:
    if i.count('WWF') <= 120:
        maxi = max(maxi, len(i))
    else:
        if len(i) > maxi:
            i = i.split('WWF')
            for j in range(len(i) - 120):
                ps = 'WWF'.join(i[j:j+121])
                maxi = max(maxi, len(ps))

print(maxi)