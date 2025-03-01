with open('Task-17-19486-file.txt') as file:
    data = [int(i) for i in file]

cnt_7 = len([i for i in data if str(i)[-1] == '7'])
ans = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = ((p1 < 0) and (p2 > 0))
    u2 = ((p1 > 0) and (p2 < 0))
    if u1 or u2:
        if p1 + p2 < cnt_7:
            ans.append(p1 + p2)
print(len(ans), max(ans))