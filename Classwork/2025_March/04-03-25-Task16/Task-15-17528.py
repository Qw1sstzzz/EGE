from itertools import combinations

def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

line = [x/5 for x in range(15*5, 63*5)]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        ans.append(A2-A1)
print(min(ans))