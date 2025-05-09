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

clustersA = [[], []]
with open('Task-27A-18677-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if (y > x - 8) and (y < x - 4):
            clustersA[0].append([x, y])
        elif (y > x - 4) and (y < 5/4 * x -  1):
            clustersA[1].append([x, y])

with open('Task-27B-18677-file.txt') as f:
    dataB = [list(map(float, i.split())) for i in f]

clustersB = []
eps = 0.9

while dataB:
    cluster = [dataB.pop()]
    for dot in cluster:
        for dot2 in dataB.copy():
            if d(dot, dot2) < eps:
                cluster.append(dot2)
                dataB.remove(dot2)
    if len(cluster) > 30:
        clustersB.append(cluster)

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 100_000
PyA = sum([y for x, y in centersA]) / 2 * 100_000
PxB = sum([x for x, y in centersB]) / 3 * 100_000
PyB = sum([y for x, y in centersB]) / 3 * 100_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))