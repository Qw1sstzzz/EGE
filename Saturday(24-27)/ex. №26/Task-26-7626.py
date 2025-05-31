with open('Task-26-7626-file.txt') as f:
    K = int(f.readline())
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)
ceils = [0]*K
ans_A, ans_B = 0, 0

for time in data:
    for i in range(K):
        if time[0] >= ceils[i]:
            ceils[i] = time[1] + 1
            ans_A += 1
            ans_B = i + 1
            break

print(ans_A, ans_B)