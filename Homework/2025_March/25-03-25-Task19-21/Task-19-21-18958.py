def f(s, m):
    if s >= 666: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+3, m-1), f(s*3, m-1), f(s + (s**2), m-1)]
    # return any(h) if m % 2 != 0 else any(h) # для 19
    return any(h) if m % 2 != 0 else all(h) # для 20-21

# print('19)', min([s for s in range(1, 666) if f(s, 2)]))
# 5
print('20)', *([s for s in range(1, 666) if not f(s, 1) and f(s, 3)]))
# 8 22
print('21)', max([s for s in range(1, 666) if not f(s, 2) and f(s, 4)]))
# 19