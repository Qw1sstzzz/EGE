with open('17.txt') as f:
    data = [int(i) for i in f]

maxi = max(data)
mini = min(data)

ans = []
for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    u1 = len(str(p1)) == 4
    u2 = len(str(p2)) == 4
    u3 = len(str(p3)) == 4
    if u1 + u2 + u3 >= 1:
        l1 = p1 % 5 == maxi % 5
        l2 = p2 % 5 == maxi % 5
        l3 = p3 % 5 == maxi % 5
        if l1 + l2 + l3 <= 1:
            k1 = p1 % 7 == mini % 7
            k2 = p2 % 7 == mini % 7
            k3 = p3 % 7 == mini % 7
            if k1 + k2 + k3 >= 2:
                ans.append(p1 + p2 + p3)

print(len(ans), max(ans))