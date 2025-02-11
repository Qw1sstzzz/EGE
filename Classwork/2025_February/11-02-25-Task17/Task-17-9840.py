with open('Task-17-9840-file.txt') as file:
    data = [int(i) for i in file]

sq_maxi = max([i for i in data if len(str(abs(i))) == 4 and str(i)[-2:] == '39'])**2
res = []

for i in range(len(data) - 1):
    ch1, ch2 = data[i], data[i+1]
    usl1 = (len(str(abs(ch1))) == 4)
    usl2 = (len(str(abs(ch2))) == 4)
    summi = ch1 + ch2
    if ((usl1 + usl2) == 1) and (summi**2 <= sq_maxi):
        res.append(summi)
print(len(res), max(res))