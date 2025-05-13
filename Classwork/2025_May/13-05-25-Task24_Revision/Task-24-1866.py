with open('Task-24-1866-file.txt') as f:
    data = f.readline()

while 'ad' in data: data = data.replace('ad', 'a d')
while 'da' in data: data = data.replace('da', 'd a')

print(len(max(data.split(), key=len)))