with open('Task-17-12735-file.txt') as file:
    data = [int(i) for i in file]

maxi = max([i for i in data if str(i)[-2:] == '09'])
ans = []
for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = (p1 % 7 == 0)
    u2 = (p2 % 7 == 0)
    u3 = (p3 % 7 == 0)
    if (u1 + u2 + u3) == 2:
        if (p1 + p2 + p3) < maxi:
            ans.append(p1*p2*p3)

print(len(ans), min(ans))