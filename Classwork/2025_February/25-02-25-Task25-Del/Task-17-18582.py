with open('Task-17-18582-file.txt') as file:
    data = [int(i) for i in file]

mini = min(data)
ans = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = p1 < 0
    u2 = p2 < 0
    u3 = p3 < 0
    if (u1 + u2 + u3) >= 2:
        summi = p1 + p2 + p3
        if str(abs(summi))[-1] == str(abs(mini))[-1]:
            ans.append(abs(summi))
print(len(ans), max(ans))