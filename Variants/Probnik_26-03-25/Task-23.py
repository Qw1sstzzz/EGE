def f(curr, end):
    if curr > end or curr == 8: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end) + f(curr * 5, end)

print(f(2, 27) * f(27, 54))