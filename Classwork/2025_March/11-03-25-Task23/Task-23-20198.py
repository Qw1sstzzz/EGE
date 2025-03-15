def f(curr, end, s):
    if curr == end and 'AAA' not in s:
        return 1
    if curr > end + 2 or 'AAA' in s:
        return 0
    return f(curr - 1, end, s + 'A') + f(curr + 5, end, s + 'B') + f(curr * 2, end, s + 'C')

print(f(5, 34, ''))