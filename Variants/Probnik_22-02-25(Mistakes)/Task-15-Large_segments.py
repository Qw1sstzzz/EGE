from math import ceil

f_usl = 1
A = 0
ans = []
for x in [k*0.25 for k in range(1, 10000000)]:
    P = 97343 <= x <= 240715
    Q = 123456 <= x <= 1345830
    R = 734652 <= x <= 1023456
    f = Q <= ((not P) <= (((not R) and (not A)) <= (not Q)))
    if f != f_usl:
        ans.append(x)

print(ceil(ans[-1] - ans[0]))