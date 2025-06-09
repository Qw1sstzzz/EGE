def f(curr, end):
    if curr > end or curr == 6 or curr == 12: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end) + f(curr + 3, end)

print(f(3, 16))