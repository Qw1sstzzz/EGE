with open('Task-17-17558-file.txt') as f:
    data = [int(i) for i in f]

length = len([i for i in data if abs(i) % 32 == 0])
ans = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = p1 < 0
    u2 = p2 < 0
    if u1 + u2 >= 1:
        if p1 + p2 < length:
            ans.append(p1 + p2)

print(len(ans), max(ans))