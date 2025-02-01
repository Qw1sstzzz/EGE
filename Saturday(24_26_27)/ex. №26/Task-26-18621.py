with open('Task-26-18621-file.txt') as file:
    N = int(file.readline())
    data = []
    for i in file:
        ID = int(i.split()[0])
        summ = sum(map(int, i.split()[1:]))
        correct = sum([int(j) for j in i.split()[1:] if int(j) > 0])
        answers = len([1 for j in i.split()[1:] if int(j) != 0])
        data.append([ID, summ, correct, answers])

data = sorted(data, key=lambda x: (-x[1], -x[2], -x[3], x[0]))

passed = [data[i] for i in range(N//4)]

last_student = data[N//4 - 1]
student_1700 = data[1699]

for i in data[N//4+1:]:
    if i[1:] == last_student[1:]:
        passed.append(i)
    elif i[1:] != last_student[1:]:
        ans_A = i
        break

ans_B = 0
for i in data:
    if i[1:] == student_1700[1:]:
        ans_B += 1

print(ans_A[0], ans_B)

# 1525 6