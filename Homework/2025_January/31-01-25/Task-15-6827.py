A = 0
f_usl = 1
for x in [k*0.25 for k in range(-10_000, 10_000)]:
    P = 257 <= x <= 1000
    Q = 5 <= x <= 100
    R = 99 <= x <= 258
    f = (A <= R) and ((not (A <= P)) <= Q)
    if f != f_usl:
        print(x)

# 0