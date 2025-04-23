with open('Task-17-21712-file.txt') as f:
    data = [int(i) for i in f]

mini = min([i for i in data if i > 0 and len(str(abs(i))) == 4 and str(abs(i))[-1] == '6'])
ans = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = (len(str(abs(p1))) == 4 and str(abs(p1))[-1] == '6')
    u2 = (len(str(abs(p2))) == 4 and str(abs(p2))[-1] == '6')
    u3 = (len(str(abs(p3))) == 4 and str(abs(p3))[-1] == '6')
    if u1 + u2 + u3 == 1:
        if (p1 + p2 + p3) <= mini:
            ans.append(p1 + p2 + p3)

print(len(ans), max(ans))