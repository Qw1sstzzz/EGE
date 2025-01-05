# from functools import *
#
# @lru_cache(None)

from sys import setrecursionlimit
setrecursionlimit(99999)

def f(start, end):
    if start < end or start == 42: return 0
    if start == end: return 1
    if start > end: return f(start-1, end) + f(start//3, end) + f(start//4, end)

print(f(2025, 250)*f(250, 25))