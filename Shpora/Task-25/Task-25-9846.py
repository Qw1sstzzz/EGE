from fnmatch import fnmatch

for x in range(123405 - 123405%2025, 10**8+1, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x // 2025)