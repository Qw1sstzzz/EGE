with open('Task-24-4627-file.txt') as f:
    data = f.readline()

data = data.replace('NPO', '*').replace('PNO', '*')
data = data.replace('N', ' ').replace('O', ' ').replace('P', ' ')

print(len(max(data.split(), key=len)))