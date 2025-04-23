from fnmatch import fnmatch

for x in range(447361 - 447361 % 7993, 10**10 + 1, 7993):
    if fnmatch(str(x), '4*4736*1'):
        print(x, x//7993)