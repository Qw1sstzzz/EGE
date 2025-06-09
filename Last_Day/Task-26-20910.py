with open('Task-26-20910-file.txt') as f:
    N, M, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

hall = [M] * (K + 1)

for h, v in data:
    hall[v] = min(hall[v], h)

ans = []
for i in range(2, K + 1):
    ans.append([min(hall[i], hall[i-1]) - 1, i - 1])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(*ans[0])