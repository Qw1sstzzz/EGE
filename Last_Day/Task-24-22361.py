from re import finditer

with open('Task-24-22361-file.txt') as f:
    data = f.readline().strip()

num = r'[1-7][0-7]*'

matches = [x.group() for x in finditer(num, data)]

ans = []

for s in matches:
    if int(s, 8) % 2 == 0:
        ans.append([len(s), s])
    else:
        if len(s) > 2:
            for p in range(len(s)):
                for l in range(len(s), p, -1):
                    ps = s[l:p]
                    if len(ps) > 2 and int(ps, 8) % 2 == 0:
                        ans.append([len(ps), ps])

ans = sorted(ans, key=lambda x: (-x[0], int(x[1], 8)))
print(data.index(ans[0][1]))
