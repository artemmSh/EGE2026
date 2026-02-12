def div(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    if len(res) == 3:
        return max(res)
    return 0


for N in range(int(106_732_567 ** 0.5), int(152_673_836 * 0.5)):
    if M := div(N ** 2):
        print(N ** 2, M)
