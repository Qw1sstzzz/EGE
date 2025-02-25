ans = []
for n in range(4, 10_000):
    s = '1' + n*'9'
    while '19' in s or '49' in s or '999' in s:
        s = s.replace('19', '9', 1)
        s = s.replace('49', '91', 1)
        s = s.replace('999', '4', 1)
    summi = sum(map(int, s))
    ans.append(summi)
print(max(ans))