def f(a, b, m):
    if a + b >= 127: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+2, b, m-1), f(a,b+2, m-1),
         f(a*3, b, m-1), f(a, b*3, m-1)]
    # return any(h) if m % 2 != 0 else any(h)
    return any(h) if m % 2 != 0 else all(h)

# print('19)', min([s for s in range(1, 123) if f(2, s, 2)]))
print('20)', *([s for s in range(1, 123) if not f(2, s, 1) and f(2, s, 3)]))
print('21)', min([s for s in range(1, 123) if not f(2, s, 2) and f(2, s, 4)]))