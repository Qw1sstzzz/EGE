def f(x, A):
    return (x % A == 0) or ((70 <= x <= 90) <= (x % 22 != 0))

for A in range(1, 10_000)[::-1]:
    if all(f(x, A) for x in range(1, 10_000)):
        print(A)
        break

# 88