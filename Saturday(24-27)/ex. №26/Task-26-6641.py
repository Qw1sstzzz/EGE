with open('Task-26-6641-file.txt') as f:
    N, M = map(int, f.readline().split())
    data = []
    for i in f:
        num, tip = i.split()
        data.append([int(num), tip])

data = sorted(data, key=lambda x: (x[0], x[1]))
products_S = []
products_W = []

for i in data.copy():
    if M >= i[0]:
        if i[1] == 'S':
            products_S.append(i[0])
            M -= i[0]
        else:
            products_W.append(i[0])
            M -= i[0]
        data.remove(i)


for p in data:
    if p[1] == 'S' and M + products_W[-1] - p[0] >= 0:
        M += products_W[-1] - p[0]
        products_S.append(p[0])
        products_W.pop()

print(len(products_S), M)






