from itertools import combinations

def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2
    return (not A) <= (B == C)

ans = []
line = [i/5 for i in range(35*5, 111*5)]

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))