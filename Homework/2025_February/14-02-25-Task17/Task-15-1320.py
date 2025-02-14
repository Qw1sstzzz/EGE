from itertools import combinations

def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = A1 <= x <= A2
    return (Q <= (not R)) and A and (not P)

line = [x/5 for x in range(9*5, 42*5)]
res = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) == 0 for x in line):
        res.append(A2 - A1)
print(max(res))