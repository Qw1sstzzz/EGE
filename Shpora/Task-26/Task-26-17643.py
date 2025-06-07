with open('Task-26-17643-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

exp = []
Avg_price = sum([i[1] for i in data]) / N
for i in data:
    if int(i[1]) > Avg_price:
        exp.append(i)

all_exp = dict()
for i in exp:
    ID, Price, State = i
    all_exp[ID] = [0, Price, 0]

for i in exp:
    ID, Price, State = i
    if State == 0:
        all_exp[ID][0] += 1
    else:
        all_exp[ID][-1] += 1

d = all_exp.values()

d = sorted(d, key=lambda x: (-x[0], -x[1], x[2]))

leader = d[0]
print(leader[0] * leader[1], leader[2])
