def f(curr, end):
    if curr < end or curr == 9 or curr == 16: return 0
    if curr == end: return 1
    if curr > end: return f(curr - 1, end) + f(curr - 2, end) + f(curr // 3, end)

print(f(19, 3))