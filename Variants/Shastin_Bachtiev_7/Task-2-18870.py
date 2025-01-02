print('x z w y F')
for x in range(2):
    for z in range(2):
        for w in range(2):
            for y in range(2):
                F = ((x <= z) <= w) or (not y)
                if F == 0:
                    print(x, z, w, y, int(F))
print('')
print('yzxw')