clustersA = [[], []]
clustersB = [[], [], []]

with open('Task-27A-18050-file.txt') as file:
    for line in file:
        x, y = [float(k) for k in line.split()]
        if y < -x + 4:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])

with open('Task-27B-18050-file.txt') as file:
    for line in file:
        x, y = [float(k) for k in line.split()]
        if y > x + 3:
            clustersB[0].append([x, y])
        elif y < -2*x + 20:
            clustersB[1].append([x, y])
        else:
            clustersB[2].append([x, y])



def d(A, B):
    xA, yA = A
    xB, yB = B
    return ((xB - xA) ** 2 + (yB - yA) ** 2 ) ** 0.5

def center(cl):
    m = []
    for z in cl:
        sm = sum(d(z, z1) for z1 in cl)
        m.append([sm, z])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]
pxA = sum(x for x, y in centersA) / 2 * 10_000
pxB = sum(x for x, y in centersA) / 3 * 10_000
pyA = sum(y for x, y in centersA) / 2 * 10_000
pyB = sum(y for x, y in centersA) / 3 * 10_000
print(int(pxA), int(pyA))
print(int(pxB), int(pyB))