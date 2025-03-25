with open('Task-17-7718-file.txt') as file:
    data = [int(i) for i in file]
ans = []
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        p1 = data[i]
        p2 = data[j]
        if p1 != p2:
            u1 = ((p1 + p2) % 18 == 0)
            u2 = ((p1 * p2) % 18 == 0)
            if u1 + u2 == 1:
                ans.append(p1 + p2)
print(len(ans), max(ans))

