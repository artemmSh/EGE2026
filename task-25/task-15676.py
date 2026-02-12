from fnmatch import fnmatch
from itertools import product
from timeit import repeat


# 1
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for D in range(22768, 10 ** 8, 22768):
    for N in range(1, 10000):
        if (not is_prime(N)) and fnmatch(str(D), f'1{N}03*6*'):
            print(D, N)
# 2
ans = []
for l1 in range(1, 5):
    for N in range(10 ** (l1 - 1), 10 ** l1):
        if not is_prime(N):
            for l2 in range(0, 4 - l1 + 1):
                for z1 in product('0123456789', repeat=l2):
                    z1 = ''.join(z1)
                    for l3 in range(0, 4 - l1 + l2 + 1):
                        for z2 in product('0123456789', repeat=l3):
                            z2 = ''.join(z2)
                            num = int(f'1{N}03{z1}6{z2}')
                            if num % 22768 == 0 and num < 10 ** 8:
                                ans.append([num, N])
for i in sorted(ans):
    print(*i)
