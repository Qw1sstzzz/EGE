A = 0
f_usl = 0
for x in [k for k in range(0, 10_000)]:
    P = 5 <= x <= 40
    Q = 41 <= x <= 54
    R = 6 <= x <= 53
    f = ((not P) <= Q) and R and (not A)
    if f != f_usl:
        print(x)

print(53 - 6)
# 47