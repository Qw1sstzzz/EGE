def triangle(n, m, k):
    maxi = max(max(n, m), k)
    if maxi < (n + m + k - maxi):
        return True
    else:
        return False

def maxx(a, b):
    if a > b: return a
    else: return b

def f(x, A):
    return triangle(A, 7, x) <= ((maxx(x+5, 14) <= 27) == (not triangle(36,21, x)))

for A in range(1, 1000)[::-1]:
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
        break

# 32