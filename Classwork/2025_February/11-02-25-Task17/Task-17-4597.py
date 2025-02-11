with open('Task-17-4597-file.txt') as file:
    data = [int(i) for i in file]

mini = min(data)
res = []

for i in range(len(data) - 1):
    ch1 = data[i]
    ch2 = data[i+1]
    usl_1 = (ch1 % 117 == mini)
    usl_2 = (ch2 % 117 == mini)
    if usl_1 + usl_2 >= 1:
        res.append([ch1 + ch2])

print(len(res), *max(res))