with open('Task-24-5237-file.txt') as f:
    data = f.readline().strip()

def check(st):
    for i in range(len(st) - 1):
        if st[i] == st[i+1]:
            return False
    return True

data = data.replace('Z', ' ')
data = data.replace('X', '*').replace('Y', '!')
data = data.split()

m = 0
for i in data:
    if m < len(i):
       if check(i):
           m = max(m, len(i))

print(m)
