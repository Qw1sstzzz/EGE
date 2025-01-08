with open('Task-26-11956-file.txt') as file:
    N_level, K_start_skill = [int(i) for i in file.readline().split()]
    data = [i.strip() for i in file.readlines()]

print(K_start_skill)

temp = []
for k in data:
    val1, val2 = k.split()
    temp.append([int(val1), int(val2)])

print(temp[:10])
temp = sorted(temp, key=lambda x: x[0])
print(temp[:100])

passed_levels = []
for i in temp:
    if i[0] <= K_start_skill:
        K_start_skill += i[1]
        passed_levels.append(i)

print(len(passed_levels), K_start_skill)

# 66 645