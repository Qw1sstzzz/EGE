with open('Task-26-file.txt') as file:
    N = int(file.readline())
    data = []
    for i in file:
        arrive, V = map(int, i.split())
        if V % 10 != 0:
            end = arrive + (V // 10 + 1)
        else:
            end = arrive + (V // 10)
        data.append([arrive, V, end])

data = sorted(data, key=lambda x: (x[2], -x[0], x[1]))

approved = [data[0]]

for i in range(N):
    if approved[-1][-1] <= data[i][0]:
        approved.append(data[i])
ans_A = len(approved)
ans_B = 0
for i in approved:
    ans_B += i[1]

print(ans_A, ans_B)