with open('Task-26-7602-file.txt') as f:
    K = int(f.readline())
    N = int(f.readline())
    time = [list(map(int, i.split())) for i in f]

luggage = [0] * K
time = sorted(time)

cnt = 0
last = 0
for t in time:
    for i in range(K):
        if t[0] >= luggage[i] + 1:
            luggage[i] = t[1]
            cnt += 1
            last = i + 1
            break

print(cnt, last)