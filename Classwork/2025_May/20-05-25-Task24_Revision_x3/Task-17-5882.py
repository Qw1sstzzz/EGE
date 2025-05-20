with open('Task-17-5882-file.txt') as f:
    data = [int(i) for i in f]

ans = []

minis = []
for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    u1 = str(p1)[-1] == '3'
    u2 = str(p2)[-1] == '3'
    if u1 + u2 == 1:
        minis.append(min(p1, p2))
minik = str(min(minis))

for i in data:
    if str(i).count('3') >= 1:
        if i >= int(minik[1])**2 + int(minik[2])**2 + int(minik[3])**2 + int(minik[4])**2:
            ans.append(i)

print(len(ans), min(ans))