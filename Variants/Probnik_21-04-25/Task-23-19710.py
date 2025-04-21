def f(curr, end):
    if curr > end or curr == 8: return 0
    if curr == end: return 1
    return f(curr + 3, end) + f(curr * 2, end)

print(f(2, 32)* f(32, 76))