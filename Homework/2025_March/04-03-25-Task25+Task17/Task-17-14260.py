with open('Task-17-14260-file.txt') as file:
    data = [int(i) for i in file]

mini = min(i for i in data if i > 0 and len(str(abs(i))) == 4 and str(i)[-2] == str(i)[-1])
res = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = len(str(abs(p1))) == 3
    u2 = len(str(abs(p2))) == 3
    u3 = len(str(abs(p3))) == 3
    if ((u1 + u2 + u3) == 3) and ((p1 + p2 + p3) > mini):
        res.append(p1 + p2 + p3)

print(len(res), max(res))
