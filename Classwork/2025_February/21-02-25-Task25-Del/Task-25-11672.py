from fnmatch import fnmatch

def f(num):
    num = str(num)
    chet = [i for i in num if int(i) % 2 == 0]
    nechet = [i for i in num if int(i) % 2 != 0]
    if len(chet) == len(nechet):
        return True
    return False


for x in range(21025, 10**10 + 1, 21025):
    if fnmatch(str(x), '12*34?5') and f(x):
        print(x, x//21025)