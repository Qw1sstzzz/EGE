clustersA = [[], []]
clustersB = [[], [], [], [], []]

with open('Task-27A-17916-file.txt') as f:
    X, Y = f.readline().split()
    for line in f:
        x, y = map(float, line.split())
        if y < 8:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

with open('Task-27B-17916-file.txt') as f:
    X, Y = f.readline().split()
    for line in f:
        x, y = map(float, line.split())
        if y > 14:
            clustersB[0].append([x, y])
        elif 10 < y < 13:
            clustersB[1].append([x, y])
        elif 6 < y < 9:
            clustersB[2].append([x, y])
        elif 4 < x < 8:
            clustersB[3].append([x, y])
        else:
            clustersB[4].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) **.5

def center(cl):
    m = []
    for c in cl:
        summ = sum([d(c, c1) for c1 in cl])
        m.append([summ, c])
    return min(m)[1]

centersA = [center(c) for c in clustersA]
centersB = [center(c) for c in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 10_000
PyA = sum([y for x, y in centersA]) / 2 * 10_000
PxB = sum([x for x, y in centersB]) / 5 * 10_000
PyB = sum([y for x, y in centersB]) / 5 * 10_000

print(int(PxA), int(PyA))
print(int(PxB), int(PyB))