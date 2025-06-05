from fnmatch import fnmatch

for x in range(1021574 - 1021574 % 2024, 10**10+1, 2024):
    if fnmatch(str(x), '1?2157*4'):
        print(x, x//2024)