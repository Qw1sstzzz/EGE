# from itertools import combinations
#
# def f(x):
#     Q = 175 <= x <= 300
#     P = 25 <= x <= 240
#     R = 270 <= x <= 340
#     A = A1 <= x <= A2
#     return (Q <= P) or ((not A) <= R)
#
# line = [x*5 for x in range(24*5, 343*5)]
# ans = []
#
# for A1, A2 in combinations(line, r=2):
#     if all(f(x) for x in line):
#         ans.append(A2 - A1)
#
# print(min(ans))

A = 0
f_usl = 1
for x in [k*0.25 for k in range(-10_000, 10_000)]:
    Q = (175 <= x <= 300)
    P = (25 <= x <= 240)
    R = (270 <= x <= 340)
    f = (Q <= P) or ((not A) <= R)
    if f != f_usl:
        print(x)

print(270-240)