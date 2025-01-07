with open('Task-24-4602-file.txt') as f:
    data = f.readline().strip()

data = data.replace('A', '*').replace('O', '*')
data = data.replace('B', '!').replace('C', '!').replace('D', '!')

data = data.replace('!*', '&')
data = data.replace('*', ' ').replace('!', ' ')
data = data.split()

print(len(max(data, key=len)))

# 174