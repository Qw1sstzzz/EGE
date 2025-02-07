from itertools import combinations

def f(x):
    P = 35 <= x <= 55
    Q = 45 <= x <= 65
    A = A1 <= x <= A2
    return (P <= A) and ((not A) <= (not Q))

line = [i/5 for i in range(30*5, 70*5)]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))
