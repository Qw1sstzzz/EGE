clustersA = [[], []]
clustersB = [[], [], []]

with open('Task-27A-20816-file.txt') as f:
    X, Y = f.readline().split()
    for line in f:
        x, y = map(float, line.split())
        if y < 0:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

with open('Task-27B-20816-file.txt') as f:
    X, Y = f.readline().split()
    for line in f:
        x, y = map(float, line.split())
        if x < -5:
            clustersB[0].append([x, y])
        elif y < -5:
            clustersB[1].append([x, y])
        else:
            clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) **.5

def center(cl):
    m = []
    for c in cl:
        summ = sum(d(c, c1) for c1 in cl)
        m.append([summ, c])
    return min(m)[1]

centersA = [center(c) for c in clustersA]
centersB = [center(c) for c in clustersB]

PxA = sum([x for x, y in centersA]) / 2 * 10_000
PyA = sum([y for x, y in centersA]) / 2 * 10_000
PxB = sum([x for x, y in centersB]) / 3 * 10_000
PyB = sum([y for x, y in centersB]) / 3 * 10_000

print(abs(int(PxA)), abs(int(PyA)))
print(abs(int(PxB)), abs(int(PyB)))