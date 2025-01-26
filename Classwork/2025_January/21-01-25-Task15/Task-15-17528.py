A = 0
f_usl = 1

for x in [l*0.25 for l in range(-10_000, 10_000)]:
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    f = P <= ((Q and (not A)) <= (not P))
    if f != f_usl:
        print(x)

print('')
print(40 - 21)

# 19