def even(num):
    num = str(num)
    res = 0
    for i in num:
        if int(i) % 2 == 0:
            res += int(i)
    return str(res**2)

def cube_diff(num):
    maxi = max(int(i) for i in str(num))
    mini = min(int(i) for i in str(num))
    return str((maxi-mini) ** 3)

for N in range(1000,10000):
    s = str(N)
    r = ''
    p1 = even(s)
    p2 = cube_diff(s)
    if int(p1) > int(p2):
        r = p2 + p1
    else:
        r = p1 + p2
    if r == '4343':
        print(N)
        break

# 1027