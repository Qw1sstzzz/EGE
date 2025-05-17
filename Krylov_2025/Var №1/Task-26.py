with open('26var01.txt') as f:
    N, M, K = map(int, f.readline().split())
    ships = [list(map(int, i.split())) for i in f]

ships = sorted(ships, key=lambda x: (x[0], -x[1]))
placed = [M + 1] * (K + 1)

ans = []
for h, w in ships:
    placed[w] = h

for i in range(1, len(placed) - 1):
    p1, p2 = placed[i], placed[i + 1]
    ans.append([min(p1, p2) - 1, i])

print()