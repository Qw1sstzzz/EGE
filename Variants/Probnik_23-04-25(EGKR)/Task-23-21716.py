def f(curr, end):
    if curr > end or curr == 56: return 0
    if curr == end: return 1
    return f(curr + 3, end) + f(curr + 7, end) + f(curr * 3, end)

print(f(12, 40) * f(40, 72) * f(72, 89))