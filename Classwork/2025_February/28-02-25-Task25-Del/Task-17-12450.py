with open('Task-17-12450-file.txt') as file:
    data = [int(i) for i in file]

mini = min([i for i in data if i % 52 == 0])
ans = []
for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = p1 % 113 + p2 % 113 + p3 % 113
    if u1 == mini:
        ans.append(p1 + p2 + p3)
print(len(ans), max(ans))
