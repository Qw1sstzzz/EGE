for x in range(1, 5556):
    s = 5**150 + 5**135 - x
    r = ''
    while s:
        r += str(s % 5)
        s //= 5
    r = r[::-1]
    if r.count('4') == 134:
        print(x)