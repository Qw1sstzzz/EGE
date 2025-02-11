with open('Task-17-17558-file.txt') as file:
    data = [int(i) for i in file]

quantity = len([i for i in data if abs(i) % 32 == 0])
res = []

for i in range(len(data) - 1):
    ch1, ch2 = data[i], data[i+1]
    usl1 = (ch1 < 0)
    usl2 = (ch2 < 0)
    if (usl1 + usl2 >= 1) and (ch1 + ch2 < quantity):
        res.append(ch1 + ch2)
print(len(res), max(res))