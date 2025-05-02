def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) **.5

def anticenter(cl):
    m = []
    for c in cl:
        summ = sum([d(c, c1) for c1 in cl])
        m.append([summ, c])
    return max(m)[1]

with open('Task-27A-21931-file.txt') as f:
    dataA = [list(map(float, i.split())) for i in f]

eps = 1
clustersA = []
while dataA:
    cluster = [dataA.pop()]
    for dot in cluster:
        for dot2 in dataA.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataA.remove(dot2)
    clustersA.append(cluster)

print([len(cl) for cl in clustersA])


with open('Task-27B-21931-file.txt') as f:
    dataB = [list(map(float, i.split())) for i in f]

eps = 1
clustersB = []
while dataB:
    cluster = [dataB.pop()]
    for dot in cluster:
        for dot2 in dataB.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataB.remove(dot2)
    clustersB.append(cluster)

print([len(cl) for cl in clustersB])

anticenterA = [anticenter(cl) for cl in clustersA]
anticenterB = [anticenter(cl) for cl in clustersB]

PxA = anticenterA[1][0] * 10_000
PyA = anticenterA[0][1] * 10_000
PxB = anticenterB[2][0] * 10_000
PyB = anticenterB[1][1] * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))
