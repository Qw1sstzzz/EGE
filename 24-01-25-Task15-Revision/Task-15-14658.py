def f(x, A):
    return ((x % 12 == 0) <= (x % 42 != 0)) or ((x + A) >= 4096)

print(max(1, 2, 3))

for A in range(1, 10_000):
    if all(f(x, A) for x in range(1, 10000)):
       print(A)
       break

# 4012