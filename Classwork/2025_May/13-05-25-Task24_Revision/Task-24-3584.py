with open('Task-24-3584-file.txt') as f:
    data = f.readline()

data = data.replace('BA', '*').replace('DA', '*')
data = data.replace('A', ' ').replace('B', ' ').replace('D', ' ')

print(len(max(data.split(), key=len)))