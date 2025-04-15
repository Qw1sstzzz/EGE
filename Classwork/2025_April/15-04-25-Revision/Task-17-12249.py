with open('Task-17-12249-file.txt') as f:
    data = [int(i) for i in f]

maxi = max([i for i in data if len(str(abs(i))) == 5 and str(abs(i))[-1] == '3'])
ans = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = str(abs(p1))[-1] == '3'
    u2 = str(abs(p2))[-1] == '3'
    u3 = str(abs(p3))[-1] == '3'
    if u1 + u2 + u3 >= 1:
        if p1 + p2 + p3 <= maxi:
            ans.append(p1 + p2 + p3)
print(len(ans), max(ans))