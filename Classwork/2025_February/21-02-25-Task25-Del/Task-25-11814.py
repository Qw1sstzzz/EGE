from fnmatch import fnmatch

for x in range(210006807 - 210006807 % 1777, 10**10+1, 1777):
    if fnmatch(str(x), '21???68?79'):
        print(x, x//1777)