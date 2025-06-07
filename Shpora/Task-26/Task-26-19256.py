with open('Task-26-19256-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)
exercises = dict()
for i in data:
    ID, Num = i
    if ID not in exercises:
        exercises[ID] = [Num]
    else:
        if Num not in exercises[ID]:
            exercises[ID].append(Num)

ans = []
for i in exercises.items():
    ID = i[0]
    Tasks = i[1]
    cnt = [1]
    c = 1
    for j in range(len(Tasks) - 1):
        if Tasks[j+1] - Tasks[j] == 1:
            c += 1
        else:
            cnt.append(c)
            c = 1
            continue
        cnt.append(c)
    cnt = max(cnt)
    ans.append([ID, cnt])

ans = sorted(ans, key=lambda x: (-x[1], x[0]))

print(*ans[0])