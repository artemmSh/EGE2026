import math
from typing import Any


def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x: object) -> int | Any:
    res = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i): res += [i]
            if is_prime(x // i): res += [x // i]
    if len(res) == 2 and res[0] * res[1] == x:
        if str(res[0]).count('5') == str(res[1]).count('5') == 1:
            return max(res)
    return 0


cnt = 0
for N in range(1_324_727 + 1, 10 ** 20):
    if M := f(N):
        cnt += 1
        print(N, M)
    if cnt == 5:
        break
