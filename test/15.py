P = list()
Q = list()
for p in range(15, 41):
    P.append(p)
for q in range(21, 64):
    Q.append(q)
for x in range(-1000000, 1000000):
    if not x in P == 1:
        print(x)