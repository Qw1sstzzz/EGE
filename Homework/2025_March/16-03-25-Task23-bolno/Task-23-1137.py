def f(curr):
    if curr == 29: return 1
    if curr > 29: return 0
    return f(curr + 1) + f(curr * 2) + f(curr * 2 + 1)

print(f(4))