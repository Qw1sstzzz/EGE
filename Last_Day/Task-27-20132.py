from itertools import combinations

with open('Task-27A-20132-file.txt') as f:
    dataA = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataA.append((float(x), float(y)))

with open('Task-27B-20132-file.txt') as f:
    dataB = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataB.append((float(x), float(y)))

from math import dist

clustersA = []
eps = 1
while dataA:
    kl = [dataA.pop()]
    for p1 in kl:
        for p2 in dataA.copy():
            if dist(p1, p2) <= eps:
                kl.append(p2)
                dataA.remove(p2)
    clustersA.append(kl)

clustersB = []
eps = 1
while dataB:
    kl = [dataB.pop()]
    for p1 in kl:
        for p2 in dataB.copy():
            if dist(p1, p2) <= eps:
                kl.append(p2)
                dataB.remove(p2)
    clustersB.append(kl)

def f(cl1, cl2):
    m = []
    for dot in cl1:
        for dot2 in cl2:
            m.append([dist(dot2, dot), (dot, dot2)])
    return min(m)[1]

cornersA = set()

for clust1, clust2 in combinations(clustersA, r=2):
    cornersA |= {*f(clust1, clust2)}

print(int(sum(c[0] for c in cornersA) / len(cornersA) * 10000))
print(int(sum(c[1] for c in cornersA) / len(cornersA) * 10000))

cornersB = set()

for clust1, clust2 in combinations(clustersB, r=2):
    cornersB |= {*f(clust1, clust2)}

print(int(sum(c[0] for c in cornersB) / len(cornersB) * 10000))
print(int(sum(c[1] for c in cornersB) / len(cornersB) * 10000))