with open('Task-17-file.txt') as file:
    data = [int(i) for i in file]

maxi = max(i for i in data if str(i)[-2:] == '50')
res = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    if p1 != p2 and p1 != p3 and p2 != p3:
        u1 = (len(str(abs(p1))) == 5)
        u2 = (len(str(abs(p2))) == 5)
        u3 = (len(str(abs(p3))) == 5)
        if (u1 + u2 + u3) == 3:
            if (p1 + p2 + p3) <= maxi:
                res.append(p1 + p2 + p3)
print(len(res), max(res))