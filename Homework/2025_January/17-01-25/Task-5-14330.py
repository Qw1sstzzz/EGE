def sq_sum(num):
    num = str(num)
    maxi = max(int(i) for i in num)
    mini = min(int(i) for i in num)
    return (maxi + mini) ** 2

def multi(num):
    r = 1
    num = str(num)
    for i in num:
        if int(i) % 2 == 0:
            r *= int(i)
    return r

ans = []
for N in range(10_000, 100_000):
    square = sq_sum(N)
    multiple = multi(N)
    if square >= multiple: R = str(square) + str(multiple)
    else: R = str(multiple) + str(square)

    if R == '12116':
        ans.append(N)
print(min(ans))