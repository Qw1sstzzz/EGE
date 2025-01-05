with open('Task-17-file.txt') as file:
    data = [int(i) for i in file]

mini = min([i for i in data if i % 2025 == 0 and i > 0])
res = []
for i in range(len(data) - 3):
    p1, p2, p3, p4 = data[i], data[i+1], data[i+2], data[i+3]
    summi = p1 + p2 + p3 + p4
    if p1 > 0 and p4 > 0:
        usl_2 = abs(p2 - p3)
        if usl_2 <= mini:
            res.append(summi)
print(len(res), min(res))