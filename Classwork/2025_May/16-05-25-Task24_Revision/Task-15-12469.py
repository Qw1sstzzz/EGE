from itertools import combinations

def f(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = A1 <= x <= A2
    return D <= (((not C) and (not A)) <= (not D))

ans = []
line = [x/5 for x in range(7*5, 100*5)]

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        ans.append(A2-A1)
print(min(ans))