with open('Task-24-11636-file.txt') as file:
    data = file.readline().strip()

A_first = data.find('A')
A_last = data.rfind('A')
data = data[A_first:A_last+1]

pos_a = [i for i in range(len(data)) if data[i] == 'A']
cnt = 0
for i in range(len(pos_a) - 1):
    if pos_a[i+1] - pos_a[i] > 1:
        cnt += 1