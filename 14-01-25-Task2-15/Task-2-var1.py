print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x <= y) and (z == (w <= x)) and (not w)
                if f:
                    print(x, y, z, w, int(f))

# yxzw
