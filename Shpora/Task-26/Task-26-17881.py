with open('Task-26-17881-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

Good_students = []
Bad_students = []

for i in data:
    ID = i[0]
    Cnt_2 = i[1:].count(2)
    Summ = sum(i[1:5])
    if Cnt_2 == 0:
        Good_students.append([ID, Summ])
    else:
        Bad_students.append([ID, Cnt_2])

Good_students = sorted(Good_students, key=lambda x: (-x[1], x[0]))
Bad_students = sorted(Bad_students, key=lambda x: (x[1], x[0]))

ans_A, ans_B = 0, 0

Stipuha = Good_students[:N // 4]

for i in Bad_students:
    if i[1] > 2:
        ans_B = i[0]
        break

print(Stipuha[-1][0], ans_B)