from itertools import combinations

def f(x):
    P = 44 <= x <= 49
    Q = 28 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

line = [x/5 for x in range(27*5, 55*5)]
ans =[]

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))