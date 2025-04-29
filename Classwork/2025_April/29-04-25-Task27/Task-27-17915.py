clustersA = [[], [], []]
clustersB = [[], [], [], []]

with open('Task-27A-17915-file.txt') as f:
    X, Y = f.readline().split()
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        if x < 6:
            clustersA[0].append([x, y])
        elif y < 23:
            clustersA[1].append([x, y])
        else:
            clustersA[2].append([x, y])

with open('Task-27B-17915-file.txt') as f:
    X, Y = f.readline().split()
    for line in f:
        x, y = map(float, line.replace(',', '.').split())
        if x < 12 and y > 16:
            clustersB[0].append([x, y])
        elif y < 9.5 and x < 15.5:
            clustersB[1].append([x, y])
        elif y < 11 and 15.5 < x < 21:
            clustersB[2].append([x, y])
        else:
            clustersB[3].append([x, y])

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

PxA = sum([x for x, y in centersA]) / 3 * 10_000
PyA = sum([y for x, y in centersA]) / 3 * 10_000
PxB = sum([x for x, y in centersB]) / 4 * 10_000
PyB = sum([y for x, y in centersB]) / 4 * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))