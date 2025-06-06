clustersA = [[], []]
clustersB = [[], [], []]

with open('Task-27A-21425-file.txt') as f:
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        if x < 15:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

with open('Task-27B-21425-file.txt') as f:
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        if x < 0:
            clustersB[0].append([x, y])
        elif y < 0:
            clustersB[1].append([x, y])
        else:
            clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) **.5

def center(cl):
    dist = []
    for c in cl:
        summ = sum(d(c, c1) for c1 in cl)
        dist.append([summ, c])
    return min(dist)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 10_000
PyA = sum([y for x, y in centersA]) / 2 * 10_000
PxB = sum([x for x, y in centersB]) / 3 * 10_000
PyB = sum([y for x, y in centersB]) / 3 * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))