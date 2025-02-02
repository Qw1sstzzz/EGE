def f(s, num):
    if s % num == 0: return 1
    else: return 0

def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1
for n in range(2, 10_000):
    if prime(n):
        s = '>' + 21*'0' + n*'1' + 11*'2'
        while '>1' in s or '>2' in s or '>0' in s:
            s = s.replace('>1', '22>')
            s = s.replace('>2', '2>')
            s = s.replace('>0', '1>')

        summi = sum([int(i) for i in s[:-1]])
        if f(summi, n):
            print(n)
            break
    else:
        pass

# 43