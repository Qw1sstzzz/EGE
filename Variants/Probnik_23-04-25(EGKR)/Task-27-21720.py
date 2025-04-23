clustersA = [[], []]
clustersB = [[], [], []]

with open('Task-27A-21720-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if y < -2:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

with open('Task-27B-21720-file.txt') as f:
    for line in f:
        x, y = map(float, line.split())
        if y < -5:
            clustersB[0].append([x, y])
        elif x < -6 and y > -5:
            clustersB[1].append([x, y])
        else:
            clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def center(cl):
    m = []
    for c in cl:
        summ = sum(d(c, cl1) for cl1 in cl)
        m.append([summ, c])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]
Px_A = sum(x for x, y in centersA) / 2 * 10_000
Px_B = sum(x for x, y in centersB) / 3 * 10_000
Py_A = sum(y for x, y in centersA) / 2 * 10_000
Py_B = sum(y for x, y in centersB) / 3 * 10_000

print(int(Px_A), int(Py_A))
print(int(Px_B), int(Py_B))

# -32540 -13646
# -47031 25263