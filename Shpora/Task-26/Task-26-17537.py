with open('Task-26-17537-file.txt') as f:
    N, M, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

hall = [M] * (K + 1)
data = sorted(data)
ans = []

for h, v in data:
    hall[v] = min(h - 1, hall[v])

for i in range(1, K + 1):
    l = min(hall[i-1], hall[i])
    ans.append([l, i])

print(*max(ans))





