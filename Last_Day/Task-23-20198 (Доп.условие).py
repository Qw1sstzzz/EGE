def f(curr, end, sh):
    if curr >= end + 3: return 0
    if 'AAA' in sh: return 0
    if curr == end: return 1
    return f(curr - 1, end, sh + 'A') + f(curr + 5, end, sh + 'B') + f(curr * 2, end, sh + 'C')

print(f(5, 34, ''))