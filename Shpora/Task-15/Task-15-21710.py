from itertools import combinations

def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2
    return (not A) <= (B == C)

line = [x + eps for x in range(36, 110) for eps in (-0.15, 0, 0.15)]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) == 1 for x in line):
        ans.append(A2 - A1)

print(min(ans))