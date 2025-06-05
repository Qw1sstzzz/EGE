with open('Task-17-17873-file.txt') as f:
    data = [int(i) for i in f]

mini = min(data)
ans = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = p1 % 16 == mini
    u2 = p2 % 16 == mini
    if u1 + u2 >= 1:
        ans.append(p1+p2)

print(len(ans), max(ans))