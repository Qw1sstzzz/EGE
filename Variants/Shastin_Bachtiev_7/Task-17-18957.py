with open('Task-17-18957-file.txt') as file:
    data = [int(i) for i in file]
res = []
maxi = max(data)
print(maxi)
for i in range(len(data) - 2):
    num1, num2, num3 = str(data[i]), str(data[i+1]), str(data[i+2])
    usl1_num1 = (num1.count('0') == 0)
    usl1_num2 = (num2.count('0') == 0)
    usl1_num3 = (num3.count('0') == 0)
    summ = int(num1) + int(num2) + int(num3)
    if ((usl1_num1 + usl1_num2 + usl1_num3) >= 2) and (summ < (maxi // 2)):
        res.append(summ)

print(len(res), max(res))

# 5072 49976