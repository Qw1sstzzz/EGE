def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

def cry(cl):
    m = []
    for c in cl:
        summ = sum([d(c, c1) for c1 in cl])
        m.append([summ, c])
    return max(m)[1]

with open('Task-27A-20497-file.txt') as f:
    dataA = [list(map(float, i.split())) for i in f]

eps = 0.5
clustersA = []

while dataA:
    cluster = [dataA.pop()]
    for dot in cluster:
        for dot2 in dataA.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataA.remove(dot2)
    if len(cluster) > 10:
        clustersA.append(cluster)

with open('Task-27B-20497-file.txt') as f:
    dataB = [list(map(float, i.split())) for i in f]

eps = 3
clustersB = []

while dataB:
    cluster = [dataB.pop()]
    for dot in cluster:
        for dot2 in dataB.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataB.remove(dot2)
    if len(cluster) > 10:
        clustersB.append(cluster)

kraysA = [cry(cl) for cl in clustersA]
kraysB = [cry(cl) for cl in clustersB]

PxA = sum([x for x,y in kraysA]) / 3 * 10_000
PyA = sum([y for x,y in kraysA]) / 3 * 10_000
PxB = sum([x for x,y in kraysB]) / 5 * 10_000
PyB = sum([y for x,y in kraysB]) / 5 * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))
