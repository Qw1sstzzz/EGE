def f(curr, end):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - 2, end) + f(curr // 2, end)

print(f(32, 14)*f(14, 1))