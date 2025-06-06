def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

def anticenter(cl):
    m = []
    for c in cl:
        summ = sum(d(c, c1) for c1 in cl)
        m.append([summ, c])
    return max(m)[1]

with open('Task-27A-19566-file.txt') as f:
    dataA = [list(map(float, i.split())) for i in f]

eps = 0.9
clustersA = []

while dataA:
    cluster = [dataA.pop()]
    for dot in cluster:
        for dot2 in dataA.copy():
            if d(dot, dot2) <= eps:
                cluster.append(dot2)
                dataA.remove(dot2)
    if len(cluster) > 15:
        clustersA.append(cluster)

with open('Task-27B-19566-file.txt') as f:
    dataB = [list(map(float, i.split())) for i in f]

eps = 3
clustersB = []

while dataB:
    cluster = [dataB.pop()]
    for dot in cluster:
        for dot2 in dataB.copy():
            if d(dot, dot2) <= eps:
                cluster.append(dot2)
                dataB.remove(dot2)
    if len(cluster) > 15:
        clustersB.append(cluster)


anticentersA = [anticenter(cl) for cl in clustersA]
anticentersB = [anticenter(cl) for cl in clustersB]

TxA = sum([x for x, y in anticentersA]) / 2 * 10_000
TyA = sum([y for x, y in anticentersA]) / 2 * 10_000

TxB = sum([x for x, y in anticentersB]) / 4 * 10_000
TyB = sum([y for x, y in anticentersB]) / 4 * 10_000

print(int(abs(TxA)), abs(int(TyA)))
print(int(abs(TxB)), abs(int(TyB)))