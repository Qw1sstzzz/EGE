with open('Task-17-9840-file.txt') as file:
    data = [int(i) for i in file]

maxi = max([i for i in data if str(abs(i))[-2:] == '39'])**2
ans = []
for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = len(str(abs(p1))) == 4
    u2 = len(str(abs(p2))) == 4
    if u1 + u2 == 1:
        if (p1 + p2) ** 2 <= maxi:
            ans.append(p1 + p2)
print(len(ans), max(ans))