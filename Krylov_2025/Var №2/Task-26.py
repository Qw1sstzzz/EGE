with open('26var02.txt') as f:
    N, M, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

fields = [M + 1] * (K + 1)

for horiz, vert in data:
    fields[vert] = min(horiz, fields[vert])

res = []
for x in range(1, K - 1):
    max_r = min(fields[x], fields[x+1], fields[x+2]) - 1
    res.append([max_r, x + 2])

print(*max(res))