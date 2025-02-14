with open('Task-17-7716-file.txt') as file:
    data = [int(i) for i in file]

res = []
maxi = max([i for i in data if ([1 for j in str(i) if int(j) % 2 != 0].count(1) == len(str(i)))])
print(maxi)

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = ([1 for i in str(p1) if int(i) % 2 == 0].count(1) == len(str(p1)))
    u2 = ([1 for i in str(p2) if int(i) % 2 == 0].count(1) == len(str(p2)))
    if (u1 + u2) >= 1:
        if (p1 + p2) > maxi:
            res.append(p1 + p2)
print(len(res), max(res))


