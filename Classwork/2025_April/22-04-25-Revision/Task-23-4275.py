def f(curr, end, sh):
    if curr > end: return 0
    if curr == end: return 1
    if sh >= 4:
        return f(curr + 2, end, 4)
    return f(curr + 2, end, sh) + \
        f(curr * 3, end, sh + 1) + f(curr * 5, end, sh + 1)

print(f(2, 200, 0))