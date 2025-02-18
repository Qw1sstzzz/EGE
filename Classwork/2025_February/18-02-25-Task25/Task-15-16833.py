from itertools import combinations

def f(x):
    A = A1 <= x <= A2
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    return (A and (not Q)) <= (P or Q)

line = [i/5 for i in range(24*5, 119*5)]
res = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        res.append(A2-A1)
print(max(res))