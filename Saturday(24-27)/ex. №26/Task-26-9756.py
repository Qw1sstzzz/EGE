with open('Task-26-9756-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (x[1], x[0]))

ans_A = [0]
cnt = 0
for i in data:
    if ans_A[-1] <= i[0]:
        ans_A.append(i[1])
        cnt += 1

ans_B = 0
ans_A.pop(-1)

for i in data:
    if i[0] >= ans_A[-1]:
        ans_B = max(ans_B, i[1])

print(cnt, ans_B)


