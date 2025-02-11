with open('Task-17-17530-file.txt') as file:
    data = [int(i) for i in file]

mini = min(data)
res = []

for i in range(len(data) - 1):
    ch1, ch2 = data[i], data[i+1]
    usl1 = (ch1 % 55 == mini)
    usl2 = (ch2 % 55 == mini)
    if (usl1 + usl2) >= 1:
        res.append(ch1 + ch2)

print(len(res), min(res))