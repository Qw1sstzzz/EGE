def f(curr, end, A=0):
    if curr > end + 1: return 0
    if curr == end: return 1
    if A == 0: return f(curr - 1, end, 1) + f(curr * 2, end) + f(curr * 3, end)
    if A == 1: return f(curr * 2, end) + f(curr * 3, end)

print(f(3, 15))