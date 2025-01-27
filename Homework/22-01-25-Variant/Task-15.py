def S(a, b, c):
    s = a * b
    if s > c: return True
    else: return False

def f(x, y, A):
    return (not S(x, y, A+13)) <= (S(28, y, 520) or S(x, 25, 800))

for A in range(-10_000, 10_000)[::-1]:
    if all(f(x, y, A) for x in range(1, 10_000) for y in range(1, 10_000)):
        print(A)
        break

# -13