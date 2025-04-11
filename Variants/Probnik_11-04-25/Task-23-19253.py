def f(curr, end):
    if curr < end or curr == 24: return 0
    if curr == end: return 1
    return f(curr - 1, end) + \
        f(curr - 6, end) + \
        f(curr // 2, end)

print(f(34, 29) * f(29, 19) * f(19, 6))