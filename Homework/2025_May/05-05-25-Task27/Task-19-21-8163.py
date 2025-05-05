def f(x, m):
    if x >= 348: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(x + 2, m - 1),
        f(x + 4, m - 1),
        f(x * 3, m - 1)
    ]
    # return any(h)
    return any(h) if m % 2 != 0 else all(h)

# print('19)', min([s for s in range(1, 348) if f(s, 2)]))
print('20)', *([s for s in range(1, 348) if not f(s, 1) and f(s, 3)]))
print('21)', min([s for s in range(1, 348) if not f(s, 2) and f(s, 4)]))