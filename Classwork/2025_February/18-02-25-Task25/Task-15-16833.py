from itertools import combinations

def f(x):
    A = A1 <= x <= A2
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    return (A and (not Q)) <= (P or Q)

line = [i + eps for i in range(24, 119) for eps in (0, 0.1, 0.9)]
res = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        res.append(A2-A1)
print(max(res))