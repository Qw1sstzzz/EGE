def dell(num, digit):
    return True if num % digit == 0 else False

f_usl = 1
A = 0

for x in [k*0.25 for k in range(-1000, 1000)]:
    P = 257 <= x <= 356
    Q = 5 <= x <= 600
    R = 59 <= x <= 228
    f = (R <= A) or ((dell(x, 3) <= P) <= (Q <= A))
    if f != f_usl:
        print(x)

print(227-59)
# 168