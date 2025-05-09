def f(curr, end, sh):
    if curr > end: return 0
    if curr == end and sh == 'C':
        return 0
    if curr == end: return 1
    return f(curr + 2, end, 'A') + f(curr + 5, end, 'B') + f(curr ** 2, end, 'C')

print(f(4, 36, ''))