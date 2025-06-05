with open('Task-17-17680-file.txt') as f:
    data = [int(i) for i in f]

mini = min(i for i in data if i > 0 and i % 41 == 0)
ans = []

for i in range(len(data) - 1):
    p1, p2 = data [i], data[i+1]
    if p1 != p2:
        if abs(p1 - p2) % mini == 0:
            ans.append(p1+p2)
print(len(ans), max(ans))