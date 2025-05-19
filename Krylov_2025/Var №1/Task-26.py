with open('26var01.txt') as f:
    N, M, K = map(int, f.readline().split())
    ships = [list(map(int, i.split())) for i in f]

ships = sorted(ships, key=lambda x: (x[0], -x[1]))
placed = [M + 1] * (K + 1)

for line in ships:
    horiz, vert = line
    placed[vert] = min(horiz, placed[vert])

res = [0, 0]
for j in range(1, K):
    max_r = min(placed[j], placed[j + 1]) - 1
    if max_r > res[0]:
        res = [max_r, j]

print(*res)