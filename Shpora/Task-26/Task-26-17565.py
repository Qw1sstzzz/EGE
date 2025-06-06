with open('Task-26-17565-file.txt') as f:
    N, S = map(int, f.readline().split())
    data = []
    for i in f:
        line = i.split()
        ID = int(line[0])
        Balls = int(line[1]) + int(line[2]) + int(line[3])
        Sobes = int(line[4])
        data.append([ID, Balls, Sobes])

data = sorted(data, key= lambda x: (-x[1], -x[2], x[0]))

ans = []
for i in range(S):
    ans.append(data[i])

balli = set()
for i in ans:
    balli.add(i[1])

balli = sorted(balli, reverse=True)
poluprohod = balli[-1]
prohod = balli[-2]

ans_A = 0
for i in ans:
    if i[1] == prohod:
        ans_A = i[0]

ans_B = 0
for j in data:
    if j[1] == poluprohod:
        ans_B += 1

print(ans_A, ans_B, prohod, poluprohod)


