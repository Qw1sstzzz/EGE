clustersA = [[], []]
clustersB = [[], [], [], []]

with open('Task-27A-19891-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if x < 3:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

with open('Task-27B-19891-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if x < 1 and y > -2:
            clustersB[0].append([x, y])
        elif y < -2:
            clustersB[1].append([x, y])
        elif y > 3:
            clustersB[3].append([x, y])
        else:
            clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return max(abs(x2 - x1), abs(y2 - y1))

def center(cl):
    m = []
    for c in cl:
        summ = sum([d(c, c1) for c1 in cl])
        m.append([summ, c])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 10_000
PyA = sum([y for x, y in centersA]) / 2 * 10_000
PxB = sum([x for x, y in centersB]) / 4 * 10_000
PyB = sum([y for x, y in centersB]) / 4 * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))