with open('Task-26-12256-file.txt') as f:
    S, N = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)
res = []

for i in range(N):
    if S >= data[i]:
        res.append(data[i])
        S -= data[i]
    else:
        break

S += res.pop(-1)
data = sorted(data, reverse=True)

for j in range(N):
    if S >= data[j]:
        res.append(data[j])
        break

print(len(res), res[-1])