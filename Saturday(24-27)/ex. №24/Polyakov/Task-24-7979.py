from re import *

def f(st):
    r = ''
    for i in range(len(st)):
        if st[i] in '+*':
            r += st[i]
        else:
            num = st[i]
            for j in range(i+1, len(st)):
                if st[j] in '+*':
                    r += str(int(num, 8))
                    num = ''
                    break
                else:
                    num += st[j]
    return r

with open('Task-24-314-file.txt') as file:
    data = file.readline()

num = r'[1-7][0-7]*|0'

reg = rf'[F]({num})([+*]({num}))+'

m = finditer(reg, data)
ans = []

for i in m:
    s = i.group()
    s = s[1:]
    ans.append([len(s), eval(f(s)), s])


print(max(ans))

