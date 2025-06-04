from string import digits, ascii_uppercase
alph = digits + ascii_uppercase

with open('Task-24-21908-file.txt') as f:
    data = f.readline().strip()

for c in alph[14:]:
    data = data.replace(c, ' ')

data = data.split()
ans = []

for i in data:
    i = i.lstrip('0')
    if len(i) > 1 and int(i, 14) % 2 == 0:
        ans.append([len(i), i])
    else:
        for l in range(len(i)):
            for p in range(len(i), l, -1):
                ps = i[l:p].lstrip('0')
                if len(ps) > 1 and int(ps, 14) % 2 == 0:
                    ans.append([len(ps), ps])

ans = sorted(ans)
print(ans[-2:])