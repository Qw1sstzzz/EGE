def f(a, b, s):
    if a + b >= 259: return s % 2 == 0
    if s == 0: return 0
    h = [
        f(a + 1, b, s - 1), f(a, b + 1, s - 1),
        f(a * 2, b, s - 1), f(a, b * 2, s - 1)
    ]
    # return any(h) if s % 2 != 0 else any(h)
    return any(h) if s % 2 != 0 else all(h)

# print('19)', min([s for s in range(1, 242) if f(17, s, 2)]))
print('20)', *([s for s in range(1, 242) if not f(17, s, 1) and f(17, s, 3)]))
print('21)', min([s for s in range(1, 242) if not f(17, s, 2) and f(17, s, 4)]))