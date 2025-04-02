def f(a, b, m):
    if a + b >= 175: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+1, b, m-1), f(a, b+1, m-1),
        f(a*3, b, m-1), f(a, b*3, m-1)
    ]
    # return any(h)
    return any(h) if m % 2 != 0 else all(h)

# print('19)', min([s for s in range(1, 155) if f(19, s, 2)]))
print('20)', min([s for s in range(1, 155) if not f(19, s, 1) and f(19, s, 3)]))
print('21)', min([s for s in range(1, 155) if not f(19, s, 2) and f(19, s, 4)]))