ans = []
for n in range(4, 1_000):
    s = '3' + n*'5'
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '35', 1)
        else:
            s = s.replace('333', '53', 1)
    ans.append(len(s))

print(max(ans))