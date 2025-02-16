with open('Task-26-file.txt') as file:
    N = int(file.readline().strip())
    data = []
    for i in file:
        start, duration = i.strip().split()
        end = int(start) + int(duration)
        data.append([int(start), end])

data = sorted(data, key= lambda x: x[1])
selected = [data[0]]

for i in data:
    if selected[-1][1] <= i[0]:
        selected.append(i)
ans_A = len(selected)

ans_B = 0

last = selected[-1]

for time in data:
    if last[1] <= time[0]:
        last = time

ans_B = last[0] - selected[-2][1]
print(ans_A, ans_B)
