

def f(curr, end, cnt=0):
    if curr == end and cnt == 51: return 1
    if curr > end: return 0
    return f(curr*4, end, cnt + 1) + f(curr+1, end, cnt + 1) + f(curr*3, end, cnt + 1)

print(f(2, 404))