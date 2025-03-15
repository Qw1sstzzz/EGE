with open('Task-24-105-file.txt') as file:
    data = file.readline().strip()
'''
data = data.replace('FA', 'F A').replace('FI', 'F I').replace('FL', 'F L')
data = data.replace('AF', 'A F').replace('AI', 'A I').replace('AL', 'A L')
data = data.replace('IF', 'I F').replace('IA', 'I A').replace('IL', 'I L')
data = data.replace('LF', 'L F').replace('LA', 'L A').replace('LI', 'L I')

data = data.split()

print(len(max(data, key=len)))
'''
m = 0
c = 0
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        m = max(m, c)
        c = 0
    c += 1
print(m)
