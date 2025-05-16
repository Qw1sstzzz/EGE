with open('Task-24-3792-file.txt') as f:
    data = f.readline().strip()

data = data.replace('D', ' ').replace('E', ' ')

print(len(max(data.split(), key=len)))