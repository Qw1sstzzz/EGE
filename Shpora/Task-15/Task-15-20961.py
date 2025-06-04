from itertools import combinations

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = A1 <= x <= A2
    return not (Q <= (((not A) and P) <= (not Q)))

line = [x + eps for x in range(15, 168) for eps in (-0.15, 0, 0.15)]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) == 0 for x in line):
        ans.append(A2-A1)

print(min(ans))