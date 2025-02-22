with open('Task-17-1-file.txt') as file:
    data = [int(i) for i in file]

maxi = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == '43')
ans = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = (len(str(abs(p1))) == 5 and str(p1)[-2:] == '43')
    u2 = (len(str(abs(p2))) == 5 and str(p2)[-2:] == '43')
    u3 = (len(str(abs(p3))) == 5 and str(p3)[-2:] == '43')
    if (u1 + u2 + u3) >= 1:
        if (p1**2 + p2**2 + p3**2) <= maxi**2:
            ans.append(p1**2 + p2**2 + p3**2)

print(len(ans), min(ans))