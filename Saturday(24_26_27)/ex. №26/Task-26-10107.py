with open('Task-26-10107-file.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: (x[1], -x[0]))
act = [data[0]]

for i in range(N):
    if data[i][0] < act[-1][1]:
        continue
    else:
        act.append(data[i])
# Получаем общее количество мероприятий, которые могут пройти

# print(len(act), abs(act[-2][1] - act[-1][0]), act[-2:], sep='\n')

idx = data.index(act[-1])
max_after_last = max(data[idx:])
print(len(act), abs(act[-2][1] - max_after_last[0]))
# 32 15