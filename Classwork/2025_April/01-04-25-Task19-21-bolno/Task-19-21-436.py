def f(a, b, m):
    if a + b > 44: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+b, b, m-1),
        f(a, b+a, m-1),
    ]
    return any(h) if m % 2 != 0 else all(h)

print('19)', min([s for s in range(1, 43) if f(11, s, 1)]))
print('20)', min([s for s in range(1, 43) if f(11, s, 2)]))
print('21)', min([(abs(s1 - s2), s1, s2) for s1 in range(1, 43) for s2 in range(1, 43) if f(s1, s2, 3)]))
