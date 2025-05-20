def plosh(a, b, c):
    if a*b > c: return True
    return False

def f(x, y, A):
    return (not plosh(x, y, A+13)) <= plosh(28, y, 520) or plosh(x, 25, 800)

for A in range(10000, -100, -1):
    if all(f(x, y, A) for x in range(1, 10000) for y in range(1, 10000)):
        print(A)
        break