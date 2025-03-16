with open('Task-26-17537-file.txt') as file:
    N, M, K = map(int, file.readline().split())
    places = [list(map(int, i.split())) for i in file]

reserved = [M + 1] * (K + 1)
places = sorted(places, key= lambda x: (x[1], -x[0]))
ans = []

for h, v in places:
    reserved[v] = h

for i in range(1, len(reserved) - 1):
    p1, p2 = reserved[i], reserved[i + 1]
    ans.append([min(p1, p2) - 1, i])

ans = sorted(ans, key=lambda x: (-x[0], -x[1]))

print(ans[0])
