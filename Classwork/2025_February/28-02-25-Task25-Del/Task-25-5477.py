def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 0
for x in range(600_001, 10**10):
    if x % 6 == 0:
        if is_prime(x - 1) * is_prime(x + 1):
            print(x - 1, x + 1)
            cnt += 1
    if cnt == 6:
        break