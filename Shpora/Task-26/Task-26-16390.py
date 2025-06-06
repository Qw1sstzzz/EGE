with open('Task-26-16390-file.txt') as f:
    S, N = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)
ans = []

for i in range(N):
    if S >= data[i]:
        ans.append(data[i])
        S -= data[i]
    else:
        break

S += ans.pop(-1)
data = sorted(data, reverse=True)

for j in range(N):
    if S >= data[j]:
        ans.append(data[j])
        break

print(len(ans), max(ans))