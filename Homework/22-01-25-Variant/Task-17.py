with open('Task-17-file.txt') as file:
    data = [int(i) for i in file]

mini = min([i for i in data if len(str(abs(i))) == 2 and str(i)[-1] == '1'])
mini = mini**2
ans = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    sq_p1, sq_p2 = p1**2, p2**2
    summi = p1 + p2
    u1 = ((sq_p1 < mini) and (sq_p2 >= mini))
    u2 = ((sq_p1 >= mini) and (sq_p2 < mini))
    if (u1 or u2) and summi >= 0:
        ans.append(summi)

print(len(ans), min(ans))