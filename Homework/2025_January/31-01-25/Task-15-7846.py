f_usl = 1
A = 1
for x in [k*0.25 for k in range(-10_000, 10_000)]:
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    f = (not ((not P) <= Q)) <= (A <= ((not Q) <= P))
    if f == f_usl:
        print(x)

print(23 - 13)
# 10