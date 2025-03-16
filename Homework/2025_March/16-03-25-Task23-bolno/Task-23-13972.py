def f(curr, end, s):
    if curr > end: return 0
    if curr == end: return 1
    if s == 0:
        return f(curr + 2, end, s + 1) + f(curr * 2, end, s + 1)
    return f(curr + 2, end, s + 1) + f(curr + 5, end, s + 1) + f(curr * 2, end, s + 1)

print(f(7, 23, 0)*f(23, 35, 1))