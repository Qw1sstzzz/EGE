with open('Task-26-2944-file.txt') as f:
    S, N = map(int, f.readline().split())
    data = [int(i) for i in f]

ans = []
data = sorted(data)

for i in data:
    if S >= i:
        ans.append(i)
        S -= i
    else:
        break

S += ans.pop(-1)
data = sorted(data, reverse=True)

for j in data:
    if S >= j:
        ans.append(j)
        break

print(len(ans), max(ans))