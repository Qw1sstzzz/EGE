def f(curr, end):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - 3, end) + f(curr // 3, end)

print(f(35, 8) * f(8, 1))