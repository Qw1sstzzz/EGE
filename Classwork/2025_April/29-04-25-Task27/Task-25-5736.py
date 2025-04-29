def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {num//i, i}
    return sorted(r)

def palindrome(num):
    st = str(num)
    if st[::-1] == st:
        return True
    return False

cnt = 0
for x in range(10**9+1, 10**15+1):
    if palindrome(x):
        divs = dell(x)
        if len(divs) > 0:
            if max(divs) % 7 == 0:
                print(x, max(divs))
                cnt += 1
    if cnt == 5:
        break