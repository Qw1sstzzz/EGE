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
clustersB = [[], [], [], [], [], []]

with open('Task-27A-21599-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if y < -7:
            clustersA[0].append([x, y])
        elif (y > -7) and (y < x - 10):
            clustersA[1].append([x, y])
        else:
            clustersA[2].append([x, y])

with open('Task-27B-21599-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if y < -5:
            clustersB[0].append([x, y])
        elif (y > -5) and (y < 0.6 * x):
            clustersB[1].append([x, y])
        elif (y > 0.6 * x) and (y < 2*x + 12):
            clustersB[2].append([x, y])
        elif (x > -9) and (y > 2*x + 12):
            clustersB[3].append([x, y])
        elif (x < -9) and (y > -3*x - 39):
            clustersB[4].append([x, y])
        else:
            clustersB[5].append([x, y])

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

PxA = sum([x for x, y in centersA]) / 3 * 10_000
PyA = sum([y for x, y in centersA]) / 3 * 10_000

PxB = sum([x for x, y in centersB]) / 6 * 10_000
PyB = sum([y for x, y in centersB]) / 6 * 10_000

print(abs(int(PxA)), abs(int(PyA)))
print(abs(int(PxB)), abs(int(PyB)))