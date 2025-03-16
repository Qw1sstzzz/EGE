def f(x, s, sh):
    if s == 24:
        return {x}
    if sh == 0:
        return f(x + 1, s + 1, 1) | f(x + 7, s + 1, 7) | f(x * 4, s + 1, 4)
    if sh == 1:
        return f(x + 7, s + 1, 7) | f(x * 4, s + 1, 4)
    if sh == 7:
        return f(x + 1, s + 1, 1) | f(x * 4, s + 1, 4)
    if sh == 4:
        return f(x + 1, s + 1, 1) | f(x + 7, s + 1, 7)
print(len(f(1, 0, 0)))