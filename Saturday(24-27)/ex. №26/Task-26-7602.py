with open('Task-26-7602-file.txt') as f:
    K = int(f.readline())
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)
camera = [0] * K
ans_A = 0
ans_B = 0

for time in data:
    for i in range(K):
        if time[0] >= camera[i]:
            camera[i] = time[1] + 1
            ans_A += 1
            ans_B = i + 1
            break

print(ans_A, ans_B)

