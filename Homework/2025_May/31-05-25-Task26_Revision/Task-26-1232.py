with open('Task-26-1232-file.txt') as f:
    S, N = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)
ans = []

for i in data:
    if S >= i:
        ans.append(i)
        S -= i
    else:
        break

S += ans.pop(-1)

for j in data[::-1]:
    if S >= j:
        ans.append(j)
        break

print(len(ans), max(ans))