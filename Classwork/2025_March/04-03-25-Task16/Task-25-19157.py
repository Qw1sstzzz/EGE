from fnmatch import fnmatch
for x in range(1035954 - 1035954 % 6437, 10**10, 6437):
    if fnmatch(str(x), '1?3*5*954'):
        print(x, x//6437)