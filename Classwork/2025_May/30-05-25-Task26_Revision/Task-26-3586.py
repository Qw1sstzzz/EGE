with open('Task-26-3586-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (-x[0], x[1]))
ans = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    if p1[0] == p2[0]:
        if abs(p1[1] - p2[1]) >= 2:
            ans.append([p1[0], p2[1] - p1[1]])

ans = sorted(ans,key=lambda x: (-x[1], -x[0]))

print(*ans[0])