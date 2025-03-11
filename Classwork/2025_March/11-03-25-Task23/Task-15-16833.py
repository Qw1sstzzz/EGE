from itertools import combinations
'''
def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

line = [x/5 for x in range(24*5, 119*5)]
ans = []

for A1, A2 in combinations(line, r=2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))
'''
# ans = []
# A = 1
# f_usl = 1
# for x in [k*0.25 for k in range(-10_000, 10_000)]:
#     P = 25 <= x <= 73
#     Q = 75 <= x <= 118
#     f = (A and (not Q)) <= (P or Q)
#     if f == f_usl:
#         print(x)