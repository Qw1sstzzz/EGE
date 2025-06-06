def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

def center(cl):
    m = []
    for c in cl:
        summ = sum([d(c, c1) for c1 in cl])
        m.append([summ, c])
    return min(m)[1]

'''
with open('Task-27A-19567-file.txt') as f:
    dataA = [list(map(float, i.split())) for i in f]

clustersA = []
eps = 1

while dataA:
    cluster = [dataA.pop()]
    for dot in cluster:
        for dot2 in dataA.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataA.remove(dot2)
    clustersA.append(cluster)

# print([len(cl) for cl in clustersA])
'''

'''
with open('Task-27B-19567-file.txt') as f:
    dataB = [list(map(float, i.split())) for i in f]

clustersB = []
eps = 0.5

while dataB:
    cluster = [dataB.pop()]
    for dot in cluster:
        for dot2 in dataB.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataB.remove(dot2)
    clustersB.append(cluster)

# print([len(cl) for cl in clustersB])
'''
clustersA = [[], []]
with open('Task-27A-19567-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if y < 0:
           clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])


clustersB = [[], [], [], [], [], []]
with open('Task-27B-19567-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if y > x + 12:
           clustersB[0].append([x, y])
        elif (y < x + 12) and (-4 <= x <= 4) and (y > 7):
            clustersB[1].append([x, y])
        elif (y < x + 10) and (y > x + 4) and (2 < y < 7):
            clustersB[2].append([x, y])
        elif (y < x + 4) and (y > 4) and (2 < x <= 10):
            clustersB[3].append([x, y])
        elif (y < x -2) and (y < 3):
            clustersB[4].append([x, y])
        else:
            clustersB[5].append([x, y])


centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 10_000
PyA = sum([y for x, y in centersA]) / 2 * 10_000
PxB = sum([x for x, y in centersB]) / 6 * 10_000
PyB = sum([y for x, y in centersB]) / 6 * 10_000

print(abs(int(PxA)), abs(int(PyA)))
print(abs(int(PxB)), abs(int(PyB)))