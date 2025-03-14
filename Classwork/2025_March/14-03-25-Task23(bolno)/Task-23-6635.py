ans = set()

def f(curr, h):
    if (curr < 0) and (h == 13):
        if curr in ans:
            return 0
        else:
            ans.add(curr)
            return 1

    if h > 13: return 0
    return f(curr - 3, h + 1) + f(curr * (-3), h + 1)

print(f(333, 0))