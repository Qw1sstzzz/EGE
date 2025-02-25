from itertools import *
from fnmatch import fnmatch

for x in range(123305708 - 123305708 % 17, 10**9 + 1, 17):
    if fnmatch(str(x), '1234?57?8'):
        print(x, x//17)
