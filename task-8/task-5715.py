from itertools import *

cnt = 0
for p in range(100):
    for k in range(100):
        for b in range(100):
            if k > p > b and k + p + b <= 15:
                cnt += 1
print(cnt)
