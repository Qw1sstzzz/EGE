with open('Task-17-19486-file.txt') as file:
    data = [int(i) for i in file]

count = len([i for i in data if str(i)[-1] == '7'])
res = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = (p1 < 0)
    u2 = (p2 < 0)
    if (u1 + u2) == 1:
        summi = p1 + p2
        if summi < count:
            res.append(summi)

print(len(res), max(res))