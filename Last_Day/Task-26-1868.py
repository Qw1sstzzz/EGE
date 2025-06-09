with open('Task-26-1868-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)
ans = []

for i in range(N - 1):
    p1, p2 = data[i:i+2]
    if p1[0] == p2[0]:
        if p2[1] - p1[1] - 1 == 2:
            ans.append([p1[0], p1[1] + 1])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))

print(*ans[0])