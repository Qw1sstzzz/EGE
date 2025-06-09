from re import *

with open('Task-24-22362-file.txt') as f:
    data = f.readline().strip()

num = r'[1-9AB][0-9A-B]*'

matches = [x.group() for x in finditer(num, data)]

ans = []
for s in matches:
    if int(s, 12) % 3 == 0:
        ans.append([len(s), s])
    else:
        if len(s) > 2:
            for r in range(len(s)):
                for l in range(len(s), r, -1):
                    ps = s[l:r]
                    if len(ps) > 2 and int(ps, 12) % 3 == 0:
                        ans.append([len(ps), ps])
                        break

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
ans = ans[0][1]
print(data.index(ans))


