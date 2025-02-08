with open('Task-26-8512-file.txt') as file:
    K = int(file.readline().strip())
    N = int(file.readline().strip())
    data = [list(map(int, i.strip().split())) for i in file]

data = sorted(data, key=lambda x: (x[0], x[1]))
cells = [0] * K
last_cell = 0
cnt = 0

for start, end in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = end
            cnt += 1
            last_cell = i + 1
            break

print(cnt, last_cell)

# 389 133 🥶
