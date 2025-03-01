def f(start, end):
    if start > end: return 0
    if start == end: return 1
    if start < end: return f(start + 2, end) + f(start + 3, end) + f(start * 2, end)

print(f(8, 35) - f(8, 20) * f(20, 30) * f(30, 35))