from  fnmatch import fnmatch
def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

for x in range(333, 10**9 + 1 , 333):
    if fnmatch(convert(x, 7), '?213*5664'):
        print(x, x//333)