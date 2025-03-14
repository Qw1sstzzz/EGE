def f(curr, end, sh=0):
    if curr > end: return 0
    if curr == end: return 1
    if sh == 1: return f(curr+2, end) + f(curr*3, end)
    if curr < end: return f(curr+2, end) + f(curr**2, end, 1) + f(curr*3, end)

print(f(2, 64))