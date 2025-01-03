def f(start, end):
    if start < end or start == 40: return 0
    if start == end: return 1
    if start > end: return f(start-3, end) + f(start//2, end) + f(start//5, end)

print(f(120, 49)*f(49, 6))

# 40