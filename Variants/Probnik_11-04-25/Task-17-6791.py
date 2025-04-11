with open('Task-17-6791-file.txt') as file:
    data = [int(i) for i in file]

mini = min([i for i in data if str(i)[-2:] == '68'])
ans = []
for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = str(p1)[-2:] == '68'
    u2 = str(p2)[-2:] == '68'
    if u1 + u2 == 1:
        if p1**2 + p2**2 >= mini**2:
            ans.append(p1**2 + p2**2)
print(len(ans), max(ans))