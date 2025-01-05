print('w x z y f')
for w in range(2):
    for x in range(2):
        for z in range(2):
            for y in range(2):
                f = not ((((((w and x) == x) or 1) <= z) or (not x)) and y)
                if int(f) == 0:
                    print(w, x, z, y, f)

# yxzw