def f(start, end):
    if start > end or start == 20 or start == 30: return 0
    if start == end: return 1
    if start < end: return f(start + 2, end) + f(start + 3, end) + f(start * 2, end)

print(f(8, 35))