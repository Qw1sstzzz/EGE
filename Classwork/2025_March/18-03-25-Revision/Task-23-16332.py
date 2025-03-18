def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr+1, end) + f(curr+2, end) + f(curr*2, end)

print(f(4, 11)*f(11, 13)*f(13, 15))