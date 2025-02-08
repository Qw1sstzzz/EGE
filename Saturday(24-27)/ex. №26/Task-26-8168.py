with open('Task-26-8168-file.txt') as file:
    K = int(file.readline().strip())
    N = int(file.readline().strip())
    data = [list(map(int, i.strip().split())) for i in file]

data = sorted(data)
cells = [0] * K
timeline = [''] * 1441
cnt = 0

for start, duration in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = start + duration
            cnt += 1
            for j in range(start + 1, start + duration):
                timeline[j] = timeline[j] + '+'
            break

ans_A = N - cnt
ans_B = timeline.count('+' * K)
print(ans_A, ans_B)
