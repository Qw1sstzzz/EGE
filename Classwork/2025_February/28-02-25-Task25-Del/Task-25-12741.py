from fnmatch import fnmatch

for x in range(174680 - 174680 % 1234, 10**10+1, 1234):
    if fnmatch(str(x), '4*5*6') and \
            fnmatch(str(x), '?74*68?'):
        print(x, x//1234)