def f(a, b, m):
    if (a + b) >= 30: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a + 1, b, m - 1),
        f(a, b + 1, m - 1),
        f(a * 2, b, m - 1),
        f(a, b * 2, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [[k, s] for k in range(1, 30) for s in range(1, 30) if f(k, s, 2)])




