def f(start, end):
    if start < end or (start == 36) or (start == 100): return 0
    if start == end: return 1
    if start > end: return f(start // 2, end) + f(start // 3, end) + f(start - 3, end)

print(f(163, 45)*f(45, 3))