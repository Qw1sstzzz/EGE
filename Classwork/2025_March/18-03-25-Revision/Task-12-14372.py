def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for n in range(4, 1_000):
    s = '>' + '0'*25 + '1'*n + '2'*25
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>',1)
        s = s.replace('>2', '2>',1)
        s = s.replace('>0', '1>',1)
    s = s[:-1]
    summi = sum([int(i) for i in s])

    if prime(summi):
        print(n)
        break