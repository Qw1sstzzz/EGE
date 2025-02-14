with open('Task-17-4705-file.txt') as file:
    data = [int(i) for i in file]

maxi = max([i for i in data if str(i)[-1] == '3'])
res = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i + 1]
    u1 = (str(p1)[-1] == '3')
    u2 = (str(p2)[-1] == '3')

    if (u1 + u2) == 1:
        if (p1**2 + p2**2) >= maxi**2:
            res.append(p1**2 + p2**2)

print(len(res), max(res))