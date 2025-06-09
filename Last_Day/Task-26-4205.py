with open('Task-26-4205-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)

ans = []

for i in range(len(data) - 2):
    p1, p2 = data[i], data[i+1]
    if p1[0] == p2[0]:
        if p2[1] - p1[1] - 1 == 13:
            ans.append([p1[0], p1[1]+1])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(*ans[0])