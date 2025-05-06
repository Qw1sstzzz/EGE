from itertools import combinations

def f(x):
    P = 257 <= x <= 1000
    Q = 5 <= x <= 100
    R = 99 <= x <= 258
    A = A1 <= x <= A2
    return (A <= R) and ((not (A <= P)) <= Q)

ans = []
line = [x + eps for x in range(5, 1001) for eps in [0, 0.1, 0.9]]

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))

# f_usl = 1
# A = 0
# for x in [k*0.25 for k in range(-10_000, 10_000)]:
#     P = 257 <= x <= 1000
#     Q = 5 <= x <= 100
#     R = 99 <= x <= 258
#     f = (A <= R) and ((not (A <= P)) <= Q)
#     if f != f_usl:
#         print(x)