with open('Task-17-2399-file.txt') as f:
    data = [int(i) for i in f]

ans = []
summ = [str(i) for i in data if i % 35 == 0]
summ_35 = 0
for i in summ:
    summ_35 += sum(map(int, i))

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = (p1 > summ_35)
    u2 = (p2 > summ_35)
    if u1 == 1 and u2 == 0:
        s = hex(p2)[2:]
        if s[-2:] == 'ef':
            ans.append(p1 + p2)

    elif u2 == 1 and u1 == 0:
        s = hex(p1)[2:]
        if s[-2:] == 'ef':
            ans.append(p1 + p2)

print(len(ans), min(ans))
