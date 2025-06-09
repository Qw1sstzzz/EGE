with open('Task-26-21719-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)
tasks = dict()
for i in data:
    ID, Exer = i
    if ID not in tasks.keys():
        tasks[ID] = [Exer]
    else:
        if Exer not in tasks[ID]:
            tasks[ID].append(Exer)

ans = []
for line in tasks.items():
    ID, Exercises = line
    cnt = 0
    c = 1
    for num in range(len(Exercises) - 1):
        if Exercises[num + 1] - Exercises[num] == 2:
            c += 1
        else:
            c = 1
        cnt = max(c, cnt)
    ans.append([ID, cnt])

ans = sorted(ans, key=lambda x: (-x[1], x[0]))
print(*ans[0])


