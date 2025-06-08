def f(curr, end):
    if curr < end or curr == 24: return 0
    if curr == end: return 1
    if curr > 9:
        return f(curr - 1, end) + f(int(curr ** 0.5), end) + f(int(str(curr)[:-1]), end)
    else:
        return f(curr - 1, end) + f(int(curr ** 0.5), end)

print(f(602, 7))