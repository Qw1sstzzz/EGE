from fnmatch import fnmatch

def f(x):
    x = str(x)
    summi = sum([int(i) for i in x if int(i) % 2 != 0])
    return summi

for x in range(124579, 10**8 + 1):
    if f(x) > 0:
        if (x % f(x) == 0) and (fnmatch(str(x), '124*5*79')):
            summ = sum([int(i) for i in str(x)])
            print(x, summ)