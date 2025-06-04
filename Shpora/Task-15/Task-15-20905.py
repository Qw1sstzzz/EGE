from itertools import combinations

def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

line = [x + eps for x in range(17, 80) for eps in (-0.15, 0, 0.15)]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) == 1 for x in line):
        ans.append(A2-A1)
print(min(ans))