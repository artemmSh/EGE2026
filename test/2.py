print('w x y z | F')
for w in (0, 1):
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                if y == 1 and z == 1 and w == 0:
                    print(w, x, y, z, '|', 1)

