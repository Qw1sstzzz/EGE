with open('Task-17-18617-file.txt') as file:
    data = [int(i) for i in file]

ost_3 = max(data) % 3
ost_7 = min(data) % 7
res = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]

    if (p1 % 3 == ost_3) or (p2 % 3 == ost_3):
        if (p1 % 7 == ost_7) or (p2 % 7 == ost_7):
            res.append(p1 + p2)

print(len(res), max(res))