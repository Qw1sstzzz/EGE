with open('Task-24-2421-file.txt') as f:
    data = f.readline().strip()

data = data.replace('D', ' ')

print(len(max(data.split(), key=len)))