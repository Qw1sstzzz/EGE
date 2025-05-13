with open('Task-24-7624-file.txt')as f:
    data = f.readline()

data = data.replace('X', '*').replace('Y', '*').replace('Z', '*')

while '**' in data: data = data.replace('**', '* *')

print(len(max(data.split(), key=len)))