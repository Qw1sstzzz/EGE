with open('Task-17-14952-file.txt') as file:
    data = [int(i) for i in file]

maxi = max(i for i in data if str(i)[-3:] == '121')
ans = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = (len(str(abs(p1))) == 4) and (abs(p1) % 2 == 0)
    u2 = (len(str(abs(p2))) == 4) and (abs(p2) % 2 == 0)
    u3 = (len(str(abs(p3))) == 4) and (abs(p3) % 2 == 0)
    if (u1 + u2 + u3) <= 1:
        if (p1 + p2 + p3) <= maxi:
            ans.append(p1 + p2 + p3)

print(len(ans), max(ans))