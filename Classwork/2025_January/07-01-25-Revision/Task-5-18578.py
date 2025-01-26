def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

for N in range(1, 10_000)[::-1]:
    s = convert(N, 4)
    if N % 4 == 0: s = '2' + s + '03'
    else: s  += convert(N % 4 * 5, 4)
    R = int(s, 4)
    if R <= 567:
        print(N)
        break

# 34