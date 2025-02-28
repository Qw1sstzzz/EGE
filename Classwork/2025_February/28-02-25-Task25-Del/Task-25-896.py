def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 1
for x in range(194441, 196501):
    if str(x)[-2:] == '93' and is_prime(x):
        print(cnt, x)
        cnt += 1