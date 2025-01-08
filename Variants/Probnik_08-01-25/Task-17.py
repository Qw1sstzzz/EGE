with open('Task-17-11949-file.txt') as file:
    data = [int(i) for i in file]

maxi = max([int(i) for i in data if str(i)[-2:] == '68'])
res = []

for idx in range(len(data) - 3):
    val1, val2, val3, val4 = str(data[idx]), str(data[idx+1]), str(data[idx+2]), str(data[idx+3])
    ln1, ln2, = len(str(abs(int(val1)))), len(str(abs(int(val2))))
    ln3, ln4 = len(str(abs(int(val3)))), len(str(abs(int(val4))))
    usl1 = ln1 == 2 and ln2 != 2 and ln3 != 2 and ln4 != 2
    usl2 = ln1 != 2 and ln2 == 2 and ln3 != 2 and ln4 != 2
    usl3 = ln1 != 2 and ln2 != 2 and ln3 == 2 and ln4 != 2
    usl4 = ln1 != 2 and ln2 != 2 and ln3 != 2 and ln4 == 2
    usl5 = ln1 == 2 and ln2 == 2 and ln3 == 2 and ln4 == 2
    if usl1 or usl2  or usl3 or usl4 or usl5:
        if (int(val1) + int(val2) + int(val3) + int(val4)) >= maxi:
            res.append(int(val1) + int(val2) + int(val3) + int(val4))
print(len(res), max(res))