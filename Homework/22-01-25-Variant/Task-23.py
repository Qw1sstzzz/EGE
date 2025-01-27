def maxi(n):
    n = str(n)
    m = max([int(i) for i in n])
    return m

def f(start, end):
    if start > end: return 0
    if start == end: return 1
    if start < end: return f(start + 2, end) + f(start + maxi(start), end)

print(f(32, 55) * f(55, 76))

# 476