def f(curr, end):
    if curr > end or curr == 17: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end)

print(f(1, 10) * f(10, 35))
