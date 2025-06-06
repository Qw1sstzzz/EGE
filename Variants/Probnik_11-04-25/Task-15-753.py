from itertools import combinations

def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = A1 <= x <= A2
    return (P == Q) <= (not A)

line = [x/5 for x in range(5*5, 31*5)]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in range(-1_000, 1_000)):
        ans.append(A2 - A1)
print(max(ans))