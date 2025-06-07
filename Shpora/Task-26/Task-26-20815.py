with open('Task-26-20815-file.txt') as f:
    N, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

astronauts = []
for i in data:
    ID = i[0]
    Balls = sum(i[1:5])
    Sobes = i[4]
    astronauts.append([ID, Balls, Sobes])

astronauts = sorted(astronauts, key=lambda x: (-x[1], -x[2], x[0]))

approved = []

for i in range(K):
    approved.append(astronauts[i])


prohod = 0
poluprohod = approved[-1][1]

for j in approved[::-1]:
    if j[1] != poluprohod:
        prohod = j[1]
        break

ans_A = 0
ans_B = 0

for k in approved:
    if k[1] == prohod:
        ans_A = k[0]

for j in astronauts:
    if j[1] == poluprohod:
        ans_B += 1

print(ans_A, ans_B)


