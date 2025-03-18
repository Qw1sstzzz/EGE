with open('Task-17-14952-file.txt') as file:
    data = [int(i) for i in file]
ans = []
maxi = max([i for i in data if str(abs(i))[-3:] == '121'])
for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = (1000 <= abs(p1) <= 9999) and (p1 % 2 == 0)
    u2 = (1000 <= abs(p2) <= 9999) and (p2 % 2 == 0)
    u3 = (1000 <= abs(p3) <= 9999) and (p3 % 2 == 0)
    if (u1 + u2 + u3) <= 1:
        if (p1 + p2 + p3) <= maxi:
            ans.append(p1 + p2 + p3)
print(len(ans), max(ans))