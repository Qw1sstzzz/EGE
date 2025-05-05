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

clustersA = [[], [], []]
clustersB = [[], [], [], [], []]

with open('Task-27A-19747-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if (x < 5) and (y > 5):
            clustersA[0].append([x, y])
        elif y < 5:
            clustersA[1].append([x, y])
        else:
            clustersA[2].append([x, y])

with open('Task-27B-19747-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if (y > x) and (y < 10):
            clustersB[0].append([x, y])
        elif (y < x) and (x < 10):
            clustersB[1].append([x, y])
        elif (10 < x < 21) and (y < 10):
            clustersB[2].append([x, y])
        elif (y > x) and (y > 10):
            clustersB[3].append([x, y])
        else:
            clustersB[4].append([x, y])

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 3 * 100_000
PyA = sum([y for x, y in centersA]) / 3 * 100_000
PxB = sum([x for x, y in centersB]) / 5 * 100_000
PyB = sum([y for x, y in centersB]) / 5 * 100_000

print(int(abs(PxA)), int(abs(PyA)))
print(int(abs(PxB)), int(abs(PyB)))