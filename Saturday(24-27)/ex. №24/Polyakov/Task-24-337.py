from re import *

with open('Task-24-337-file.txt') as f:
    data = f.readline()

alph = '0123456789ABCD'
num = rf'1[{alph}]*'


matches = finditer(num, data)
ans = []
for i in matches:
    num = i.group()
    for j in range(len(num) - 1):
        if num[j] != '1':
            continue
        for k in range(j+1, len(num)):
            if int(num[j:k+1], 14) % 7 == 0:
                ans.append(len(num[j:k+1]))

print(max(ans))