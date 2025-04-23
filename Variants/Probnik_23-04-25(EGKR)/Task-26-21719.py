with open('Task-26-21719-file.txt') as f:
    N = int(f.readline())
    t = [list(map(int, i.split())) for i in f]

t = sorted(t, key=lambda x: (x[0], x[1]))
data = []

ans = dict()
for i in t:
    if i not in data:
        ans[i[0]] = []
        data.append(i)

for i in data:
    ans[i[0]].append(i[1])

res = []
for j in ans.items():
    cnt = [1]
    values = j[1]

    for c in range(len(values) - 1):
        if values[c + 1] - values[c] == 2:
            cnt[-1] += 1
        else:
            cnt.append(1)

    res.append([j[0], max(cnt)])

res = sorted(res, key=lambda x: (-x[1], x[0]))
print(*res[0])