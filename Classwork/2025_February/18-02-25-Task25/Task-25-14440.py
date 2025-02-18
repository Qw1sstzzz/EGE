from fnmatch import fnmatch

def prime(num):
    for x in range(2, int(num * 0.5) + 1):
        if num % x == 0:
            return False
    return True

def multiply(num):
    r = 1
    for i in str(num):
        r *= int(i)
    return r

for x in range(315670, 10**7):
    if fnmatch(str(x), '31*567?') and prime(x):
        print(x, multiply(x))