from itertools import *

def f1(arr):
    maxi = max(arr)
    if maxi < sum(arr) - maxi:
        return True
    return False

def f2(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(2) == 2 and cnt.count(1) == 2:
        return True
    return False

with open('Task-9-4614-file.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)
