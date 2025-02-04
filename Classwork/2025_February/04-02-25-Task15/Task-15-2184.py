f_usl = 1
A = 1
for x in [k*0.25 for k in range(-10_000, 10_000)]:
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    f = (P <= (not Q)) <= (not A)
    if f == f_usl:
        print(x)

print(39 - 23)