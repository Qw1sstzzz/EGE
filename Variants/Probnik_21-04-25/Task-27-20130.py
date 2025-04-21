from math import *
clustersA = [[], []]
clustersB = [[], [], []]

with open('Task-27A-20130-file.txt') as file:
    for line in file:
        x, y = map(float, line.split())
        if x < 2:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

with open('Task-27B-20130-file.txt') as file:
    for line in file:
        x, y = map(float, line.split())
        if y < 2:
            clustersB[0].append([x, y])
        elif y > 7:
            clustersB[2].append([x, y])
        else:
            clustersB[1].append([x, y])

def diag(claster):
    mx = 0
    points = []
    for point1 in claster:
        for point2 in claster:
            if dist(point1, point2) > mx:
                mx = dist(point1, point2)
                points = [point1, point2]
    return points

diagA = [diag(cl) for cl in clustersA]
diagB = [diag(cl) for cl in clustersB]
pxA = sum(x for x, y in diagA) / 2 * 10_000
pyA = sum(y for x, y in diagA) / 2 * 10_000
pxB = sum(x for x, y in diagB) / 2 * 10_000
pyB = sum(y for x, y in diagB) / 2 * 10_000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))

print(clustersA)