def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) **.5

def center(cl):
    m = []
    for c in cl:
        summ = sum(d(c, c1) for c1 in cl)
        m.append([summ, c])
    return min(m)[1]

with open('Task-27A-21911-file.txt') as f:
    dataA = [list(map(float, i.split())) for i in f]

eps = 2
clustersA = []

while dataA:
    cluster = [dataA.pop()]
    for dot in cluster:
        for dot2 in dataA.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataA.remove(dot2)
    clustersA.append(cluster)

print([len(clust) for clust in clustersA]) # Нужно, чтобы было 2 списка

with open('Task-27B-21911-file.txt') as f:
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

print([len(clust) for clust in clustersB]) # Нужно, чтобы было 3 списка

centersA = [center(c) for c in clustersA]
centersB = [center(c) for c in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 10_000
PyA = sum([y for x, y in centersA]) / 2 * 10_000

PxB = sum([x for x, y in centersB]) / 3 * 10_000
PyB = sum([y for x, y in centers2B]) / 3 * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))

