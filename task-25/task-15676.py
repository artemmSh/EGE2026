from fnmatch import fnmatch


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
