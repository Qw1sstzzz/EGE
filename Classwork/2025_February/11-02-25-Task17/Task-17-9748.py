with open('Task-17-9748-file.txt') as file:
    data = [int(i) for i in file]

maxi = max(i for i in data if str(i)[-2:] == '15')
res = []

for i in range(len(data) - 2):
    ch1, ch2, ch3 = data[i], data[i+1], data[i+2]
    usl_length1 = (1000 <= ch1 <= 9999)
    usl_length2 = (1000 <= ch2 <= 9999)
    usl_length3 = (1000 <= ch3 <= 9999)
    if (usl_length1 + usl_length2 + usl_length3) == 1:
        summi = ch1 + ch2 + ch3
        if summi >= maxi:
            res.append(summi)

print(len(res), max(res))