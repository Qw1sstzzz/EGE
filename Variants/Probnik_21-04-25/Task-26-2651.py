with open('Task-26-2651-file.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: (x[0], x[1]))

collected_marks = []
for i in data:
    if i not in collected_marks:
        collected_marks.append(i)

d = dict()

for i in collected_marks:
    year, variant = i[0], i[1]
    if year not in d.keys():
        d[year] = 1
    else:
        d[year] += 1

ans_A = 8 * 31
ans_B = []
for i in d.items():
    ans_A -= i[1]
    ans_B.append([8 - i[1], i[0]])

ans_B = sorted(ans_B, key=lambda x: (-x[0], -x[1]))
print(ans_A, ans_B[0][1])