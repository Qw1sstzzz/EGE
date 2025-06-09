from re import *

with open('Task-24-17685-file.txt') as f:
    data = f.readline().strip()

num = r'(0|[1-9][0-9]*)'

reg = rf'{num}([+*]{num})+'

reg = rf'(?=({reg}))'

matches = [x.group(1) for x in finditer(reg, data)]
ans = []
maxi = 0
for i in matches:
    if len(i) > maxi and eval(i) == 0:
        ans.append([len(i), i])
        maxi = max(len(i), maxi)
    else:
        if len(i) > 2 and len(i) > maxi:
            for p in range(len(i)):
                for l in range(len(i), p, -1):
                    ps = i[l:p]
                    if len(ps) > 2 and eval(ps) == 0:
                        ans.append([len(ps), ps])
                        maxi = max(len(ps), maxi)
                        break

ans = sorted(ans, key=lambda x: -x[0])

print(max(ans))
