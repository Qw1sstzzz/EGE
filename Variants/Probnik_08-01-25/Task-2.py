print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or (not y)) and (not (x == z)) and w
                if f == 1:
                    print(x, y, z, w, int(f))
print('')
print('zyxw')