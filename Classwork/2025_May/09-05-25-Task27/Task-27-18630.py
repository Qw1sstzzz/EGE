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

with open('Task-27A-18630-file.txt') as f:
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
    if len(cluster) > 30:
        clustersA.append(cluster)

clustersB = [[], [], []]

with open('Task-27B-18630-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if x > 9.5 and y < 6.5:
            clustersB[0].append([x, y])
        elif 2.9 < x < 9.1 and y < -0.5*x + 10.5:
            clustersB[1].append([x, y])
        elif 4 < x < 13.5 and y > -0.3 * x + 12:
            clustersB[2].append([x, y])

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 100_000
PyA = sum([y for x, y in centersA]) / 2 * 100_000

PxB = sum([x for x, y in centersB]) / 3 * 100_000
PyB = sum([y for x, y in centersB]) / 3 * 100_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))