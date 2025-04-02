def f(curr, end, k):
    if curr > end + 1:
        return 0
    if curr == end:
        return 1
    else:
        if k == 1:
            return f(curr * 2, end, k - 1) + f(curr * 3, end, k - 1)
        else:
            return f(curr - 1, end, k + 1) + f(curr * 2, end, k) + f(curr * 3, end, k)


print(f(3, 15, 0))