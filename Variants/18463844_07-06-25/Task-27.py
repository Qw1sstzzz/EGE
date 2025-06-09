def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

def center(cl):
    m = []
    for c in cl:
        summ = sum(d(c, c1) for c1 in cl)
        m.append([summ, c])
    return min(m)[1]

clustersA = [[], []]
with open('27A.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if y < 10:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

clustersB = []
with open('27B.txt') as f:
    dataB = [list(map(float, i.split())) for i in f]

eps = 2

while dataB:
    cluster = [dataB.pop()]
    for dot in cluster:
        for dot2 in dataB.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataB.remove(dot2)
    clustersB.append(cluster)

print([len(c) for c in clustersA])
print([len(c) for c in clustersB])

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 10_000
PyA = sum([y for x, y in centersA]) / 2 * 10_000

PxB = sum([x for x, y in centersB]) / 3 * 10_000
PyB = sum([y for x, y in centersB]) / 3 * 10_000

print(abs(int(PxA)), abs(int(PyA)))
print(abs(int(PxB)), abs(int(PyB)))
