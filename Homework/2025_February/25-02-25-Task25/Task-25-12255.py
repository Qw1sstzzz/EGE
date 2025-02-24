from fnmatch import fnmatch

for x in range(1203456009 - 1203456009 % 98591, 10**12+1, 98591):
    if fnmatch(str(x), '12?3*456??9'):
        print(x, x//98591)