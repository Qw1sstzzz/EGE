with open('Task-17-13882-file.txt') as file:
    data = [int(i) for i in file]

maxi = max(i for i in data if i % 401 == 0)
res = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i], data[i+1], data[i+2]
    sm1 = sum(int(i) for i in str(p1))
    sm2 = sum(int(i) for i in str(p2))
    sm3 = sum(int(i) for i in str(p3))
    if sm1 != sm2 and sm2 != sm3 and sm3 != sm1:
        if (p1 + p2 + p3) > maxi:
            res.append(p1 + p2 + p3)
print(len(res), min(res))