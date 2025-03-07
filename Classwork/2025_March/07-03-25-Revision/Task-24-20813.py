with open('Task-24-20813-file.txt') as file:
    data = file.readline().strip()

data = data.replace('-', '*')
data = data.replace('7', '9').replace('8', '9')
data = data.replace('* ', ' ').replace(' *', ' ')
while '**' in data: data = data.replace('**', ' ')

for i in range(1, 100):
    data = data.replace(f'*{'0'*i}9', '*0 9')
    data = data.replace(f' {'0' * i}9', ' 9')

for i in range(2, 100):
    data = data.replace(f'*{'0' * i}*', '*0 0*')

data = data.split()
print(len(max(data, key=len)))

# 111