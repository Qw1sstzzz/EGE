with open('Task-17-19249-file.txt') as file:
    data = [int(i) for i in file]

maxi = max([i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == '43'])
res = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i],data[i + 1], data[i + 2]
    u1 = (str(p1)[-2:] == '43' and len(str(abs(p1))) == 5)
    u2 = (str(p2)[-2:] == '43' and len(str(abs(p2))) == 5)
    u3 = (str(p3)[-2:] == '43' and len(str(abs(p3))) == 5)

    if (u1 + u2 + u3) >= 1:
        if (p1**2 + p2**2 + p3**2) <= maxi**2:
            res.append(p1**2 + p2**2 + p3**2)

print(len(res), min(res))