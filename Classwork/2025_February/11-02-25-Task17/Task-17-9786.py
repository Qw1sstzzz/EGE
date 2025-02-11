with open('Task-17-9786-file.txt') as file:
    data = [int(i) for i in file]

maxi = max([i for i in data if str(i)[-2:] == '25'])
res = []

for i in range(len(data) - 2):
    ch1 , ch2, ch3 = data[i], data[i+1], data[i+2]
    usl1 = len(str(abs(ch1))) == 4
    usl2 = len(str(abs(ch2))) == 4
    usl3 = len(str(abs(ch3))) == 4
    summi = ch1 + ch2 + ch3
    if ((usl1 + usl2 + usl3) <= 2) and (summi <= maxi):
        res.append(summi)

print(len(res), max(res))