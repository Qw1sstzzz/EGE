with open('Task-26-10107-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (x[1], x[0]))
ans = [data[0]]

for i in range(1, N):
    if data[i][0] >= ans[-1][1]:
        ans.append(data[i])
    else:
        continue

data = sorted(data, reverse=True)
ans.pop()

for j in range(N):
    if data[j][0] >= ans[-1][1]:
        ans.append(data[j])

print(len(ans), ans[-1][0] - ans[-2][1])
