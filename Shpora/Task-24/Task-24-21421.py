from string import digits,ascii_uppercase
alph = digits + ascii_uppercase

with open('Task-24-21421-file.txt') as f:
    data = f.readline().strip()

for c in alph[12:]:
    data = data.replace(c, ' ')

ans = []
data = data.split()

for i in data:
    i = i.lstrip('0')
    if len(i) > 1:
        if int(i, 12) % 2 == 0:
            ans.append([len(i), i])
    else:
        while len(i) > 1 and int(i, 12) % 12 != 0:
            i = i[:-1]
        if len(i) > 2:
            if int(i, 12) % 12 == 0:
                ans.append([len(i), i])
ans = sorted(ans)
print(ans[-2:])
