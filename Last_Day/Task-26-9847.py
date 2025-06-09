with open('Task-26-9847-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

timeline = [0] * (60*24)

for i in data:
    start, end = i
    for k in range(start, end):
        timeline[k] += 1
res = []
peak = max(timeline)
cnt = 1

for l in range(len(timeline)):
    if timeline[l] == peak:
        res.append(l)

for k in range(len(res) - 1):
    if res[k+1] - res[k] != 1:
        cnt += 1

print(cnt, peak)