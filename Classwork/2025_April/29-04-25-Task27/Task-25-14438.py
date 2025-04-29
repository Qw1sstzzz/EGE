from fnmatch import *
def f(num):
    st = str(num)
    summ = sum(map(int, st))
    if summ**0.5 == int(summ**0.5):
        return True
    return False

for x in range(1746008  - 1746008 % 86513, 10**12+1, 86513):
    if fnmatch(str(x), '17*46??8'):
        if f(x):
            print(x, x//86513)