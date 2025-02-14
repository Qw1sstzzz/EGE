with open('Task-24-15339-file.txt') as file:
    data = file.readline().strip()

data = data.replace('B', 'A').replace('C', 'A')
data = data.replace('7', '6').replace('8', '6').replace('9', '6')
while 'AA' in data:
    data = data.replace('AA', 'A A')
while '66' in data:
    data = data.replace('66', '6 6')
data = data.split()
print(len(max(data, key=len)))
