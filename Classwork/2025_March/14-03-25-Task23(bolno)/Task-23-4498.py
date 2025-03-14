def f(curr, end, A, B, C):
    if curr == end and A <= 4 and B >= 2 and C == 5:
        return 1
    if curr > end: return 0
    return f(curr * 5, end, A + 1, B, C) + \
        f(curr * 3, end, A, B + 1, C) + \
        f(curr + 45, end, A, B, C + 1)
print(f(1,2970, 0, 0, 0))