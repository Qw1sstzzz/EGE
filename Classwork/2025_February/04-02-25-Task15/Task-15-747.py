from itertools import *

def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

line = [40, 43, 44, 49, 53, 55]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x / 5) for x in range(A1 * 5 - 1, A2 * 5 + 1)):
        ans.append(A2 - A1)
print(max(ans))