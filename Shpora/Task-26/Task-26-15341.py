with open('Task-26-15341-file.txt') as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data, reverse=True)

ans = [data[0]]

for i in range(1, N):
    if ans[-1] - data[i] >= 8:
        ans.append(data[i])

print(len(ans), ans[-1])