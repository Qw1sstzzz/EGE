for N in range(2, 10_000):
    s = bin(N)[2:]
    cnt_0_on_chet_pos = len([s[i] for i in range(len(s)) if s[i] == '0' and i % 2 != 0])
    cnt_1_on_nechet_pos = len([s[i] for i in range(len(s)) if s[i] == '1' and i % 2 == 0])
    R = abs(cnt_1_on_nechet_pos - cnt_0_on_chet_pos)
    if R == 5:
        print(N)
        break
