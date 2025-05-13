with open('Task-24-7600-file.txt')as f:
    data = f.readline()

data = data.replace('Q', '*').replace('R', '*').replace('S', '*')

while '**' in data: data = data.replace('**', '* *')

print(len(max(data.split(), key=len)))