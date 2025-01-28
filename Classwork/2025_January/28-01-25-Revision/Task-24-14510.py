with open('Task-24-14510-file.txt') as file:
    data = file.readline().strip()

gl = 'AEIOUY'
for c in gl:
    data = data.replace(c, '*')

for x in 'QWRTPSDFGHJKLZXCVBNM':
    data = data.replace(x, '!')

data = data.replace('!!*', '%')
# data = data[data.find('%'):data.rfind('%')]
data = data.split('%')

mini = 10*10000
for i in range(len(data) - 499):
    s = '%%%'.join(data[i:i+499])
    # получается строка типа ...ssg...ssg... (т.е. обрезаются первые и последние согл+согл+гл)
    mini = min(len(s), mini)

print(mini)

