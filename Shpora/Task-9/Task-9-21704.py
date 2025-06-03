with open('Task-9-21704-file.txt') as f:
    data = [list(map(int, i.split())) for i in f]

def f1(arr):
    if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] > arr[6]:
        return True
    return False

def f2(arr):
    if ((min(arr) + max(arr)) / 2) > ((sum(arr) - min(arr) - max(arr)) / 5):
        return True
    return False

for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break