def f(curr, end):
    if curr > end or curr == 21: return 0
    if curr == end: return 1
    return f(curr + 2, end) + f(curr + 3, end) + f(curr * 2, end)

print(f(7, 14) * f(14, 32))