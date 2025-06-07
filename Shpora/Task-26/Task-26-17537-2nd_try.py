with open('Task-26-17537-file.txt') as f:
    N, M, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

seats = [M] * (K + 1)

for h, v in data:
    seats[v] = min(h - 1, seats[v])

ans = []
for j in range(2, K+1):
    ans.append([min(seats[j], seats[j-1]), j])

print(*max(ans))