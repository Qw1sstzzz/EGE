
print(15//2)
def f(a, b, m):
    if a + b <= 100: return m % 2 == 0
    if m == 0: return 0
    h = [f(a-3, b-3, m-1), f(a//2, b, m-1), f(a, b//2, m-1)]
    # return any(h) if m % 2 != 0 else any(h)
    return any(h) if m % 2 != 0 else all(h)

# print('19)', min(s for s in range(53, 1_000) if f(48, s, 2)))
print('20)', *(s for s in range(53, 1_000) if not f(48, s, 1) and f(48, s, 3)))
print('21)', min(s for s in range(53, 1_000) if not f(48, s, 2) and f(48, s, 4)))