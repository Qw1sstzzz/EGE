clustersA = [[], []]
clustersB = [[], [], []]

for line in open('Task-27-20816-A-file.txt'):
    x, y = [float(i) for i in line.split()]
    if y < 0:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for line in open('Task-27-20816-B-file.txt'):
    x, y = [float(i) for i in line.split()]
    if x < -5:
        clustersB[0].append([x, y])
    elif y < -2:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1)**2 + (y2 - y1)**2) **0.5

def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]

pxA = sum(x for x, y in centersA) / 2 * 10000
pyA = sum(y for x, y in centersA) / 2 * 10000
pxB = sum(x for x, y in centersB) / 3 * 10000
pyB = sum(y for x, y in centersB) / 3 * 10000

print(int(abs(pxA)), int(abs(pyA)))
print(int(abs(pxB)), int(abs(pyB)))