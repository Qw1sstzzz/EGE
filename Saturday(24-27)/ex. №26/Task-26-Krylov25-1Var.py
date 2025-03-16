with open('Task-26-Krylov25-1Var-file.txt') as file:
    N, M, K = map(int, file.readline().split())
    ships = [list(map(int, i.split())) for i in file]

ships = sorted(ships, key=lambda x: (x[1], -x[0]))
ans = []

pole = [M + 1] * (K + 1)
for hor, vert in ships:
    pole[vert] = hor

# i = столбец (размещение по горизонтали)
for i in range(1, len(pole) - 1):
    p1, p2 = pole[i:i+2]
    ans.append([min(p1, p2) - 1, i])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))

print(ans[0])