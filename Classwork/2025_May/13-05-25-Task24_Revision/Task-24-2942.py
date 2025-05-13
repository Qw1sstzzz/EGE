with open('Task-24-2942-file.txt') as f:
    data = f.readline()

data = data.replace('AB', '!').replace('AC', '*')
data = data.replace('A', ' ').replace('B', ' ').replace('C', ' ')

print(len(max(data.split(), key=len)))