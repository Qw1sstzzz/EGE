def f(curr, end, cnt):
    if curr == end and cnt <= 15: return 1
    if curr > end: return 0
    return f(curr + 2, end, cnt + (1 if (curr + 2) % 2 == 0 else 0)) \
        + f(curr + 3, end, cnt + (1 if (curr + 3) % 2 == 0 else 0)) \
        + f(curr * 2 + 1, end, cnt + (1 if (curr * 2 + 1) % 2 == 0 else 0))

print(f(1, 55, 0))