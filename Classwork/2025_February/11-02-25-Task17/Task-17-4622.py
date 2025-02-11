with open('Task-17-4622-file.txt') as file:
    data = [int(i) for i in file]

mini = min([i for i in data if i > 0 and i % 19 == 0])
res = []

for i in range(len(data) - 1):
    ch1, ch2 = data[i], data[i+1]
    summi = ch1 + ch2
    if summi < mini:
        res.append([summi, ch1, ch2])
maxi = max(res)
ans_B = sum(maxi[1:])
print(len(res), ans_B)
