with open('Task-9-9778-file.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(arr):
    count = [arr.count(i) for i in arr]
    return count.count(2) == 2 and count.count(1) == 4

def f2(arr):
    c = [i for i in arr if arr.count(i) > 1]
    ch = c[0]
    no_repeat = [i for i in arr if arr.count(i) == 1]
    avg = sum(no_repeat) / len(no_repeat)
    return ch >= avg

cnt = 0
for pos, i in enumerate(data, start=1):
    if f1(i) and f2(i):
        print(pos)
        break

