ans = []
for n in range(4, 10_000):
    s = '1' + '2'*n
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    ans.append(sum(map(int, s)))

print(max(ans))