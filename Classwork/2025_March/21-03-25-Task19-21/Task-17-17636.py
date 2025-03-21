with open('Task-17-17636-file.txt') as file:
    data = [int(i) for i in file]

maxi = max(i for i in data if str(abs(i))[-1] == '3' and len(str(abs(i))) == 3)
ans = []
for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = (str(p1)[-1] == '3' and len(str(abs(p1))) == 3)
    u2 = (str(p2)[-1] == '3' and len(str(abs(p2))) == 3)
    u3 = (str(p3)[-1] == '3' and len(str(abs(p3))) == 3)
    if (u1 + u2 + u3) >= 1:
        if (p1 + p2 + p3) < maxi:
            ans.append(p1 + p2 + p3)
print(len(ans), max(ans))