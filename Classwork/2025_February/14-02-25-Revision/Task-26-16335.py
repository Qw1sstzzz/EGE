with open('Task-26-16335-file.txt') as file:
    N = int(file.readline().strip())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)

korzh = data[0]
cnt = 1

for i in data:
    if korzh - i >= 4:
        cnt += 1
        korzh = i

print(cnt, korzh)
# 2172 50