with open('Task-24-8510-file.txt')as f:
    data = f.readline()

data = data.replace('N', '*').replace('O', '*').replace('P', '*')

while '**' in data: data = data.replace('**', '* *')

print(len(max(data.split(), key=len)))