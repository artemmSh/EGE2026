from itertools import *

ans = set()
for A in product('01234', repeat=5):
    for B in product('01234', repeat=5):
        vala = ''.join(A)
        valb = ''.join(B)
        if vala[0] != '0' and valb[0] != '0' and int(vala, 5) > int(valb, 5):
            ans.add(int(vala, 5) - int(valb, 5))
print(len(ans))
