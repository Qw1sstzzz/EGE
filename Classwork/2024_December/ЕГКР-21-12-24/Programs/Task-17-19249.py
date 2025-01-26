with open('Task-17-19249-file.txt') as file:
    data = [int(i) for i in file]
res = []
maxi = max(i for i in data if len(str(i))==5 and str(i)[-2:]=='43')

for idx in range(len(data) - 2):
    val1, val2, val3 = (data[idx], data[idx+1], data[idx+2])
    ysl_ch1 = len(str(abs(val1))) == 5 and str(val1)[-2:] == '43'
    ysl_ch2 = len(str(abs(val2))) == 5 and str(val2)[-2:] == '43'
    ysl_ch3 = len(str(abs(val3))) == 5 and str(val3)[-2:] == '43'
    ysl_summ = maxi**2 >= (val1**2 + val2**2 + val3**2)
    if (ysl_ch1 or ysl_ch2 or ysl_ch3) and ysl_summ:
        res.append(val1**2 + val2**2 + val3**2)

print(len(res), min(res))