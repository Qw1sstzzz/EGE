with open('Task-17-file.txt') as file:
    data = [int(i) for i in file]

mini = min([i for i in data if str(abs(i))[-2:] == '19' and len(str(abs(i))) == 3])
ans = []
for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = (str(abs(p1))[-2:] == '19' and len(str(abs(p1))) == 5)
    u2 = (str(abs(p2))[-2:] == '19' and len(str(abs(p2))) == 5)
    u3 = (str(abs(p3))[-2:] == '19' and len(str(abs(p3))) == 5)
    if (u1 + u2 + u3) >= 1:
        if (p1 + p2 + p3) > (mini**2):
            ans.append(p1 + p2 + p3)
print(len(ans), min(ans))