s = 5*729**2024 + 3*243**1413 - 7*81**169 - 2*9**107 + 3017
ans = 0

while s:
    ost = s % 27
    if ost % 2 == 0 and ost < 25:
        ans += ost
    s //= 27
print(ans)