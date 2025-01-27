with open('Task-24-file.txt') as file:
    data = file.readline()

data = data.replace('N', '*').replace('O', '*').replace('P', '*')
while '**' in data:
    data = data.replace('**', '* *')
data = data.split()
print(len(max(data, key=len)))

# 57