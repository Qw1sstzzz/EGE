def f(a, b, nums=frozenset()):
    if a == b: return 1

    if a in nums or abs(a) > 50:
        return 0
    res = 0
    for s in (a + 2, a - 3):
        res += f(s, b, nums | {a})
    return res

print(f(1, 30))