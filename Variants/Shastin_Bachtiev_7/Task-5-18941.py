res = []
for N in range(1000, 10000):
    s = str(N)
    p_1_2 = int(s[0]) * int(s[1])
    p_1_3 = int(s[0]) * int(s[2])
    p_1_4 = int(s[0]) * int(s[3])
    maxi_1 = max(p_1_4, max(p_1_2, p_1_3))
    if maxi_1 == p_1_2:
        maxi_2 = max(p_1_3, p_1_4)
    elif maxi_1 == p_1_3:
        maxi_2 = max(p_1_2, p_1_4)
    elif maxi_1 == p_1_4:
        maxi_2 = max(p_1_2, p_1_3)
    R = str(maxi_2) + str(maxi_1)
    if R == '5472':
        res.append(N)
print(min(res))
# 9068
