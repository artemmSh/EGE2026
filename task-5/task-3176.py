def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = converter(N, 9)
    for q in range(5):
        if R.count('5') == R.count('7'):
            R += R[-1]
        else:
            R += str(max([k for k, v in {int(i): R.count(i) for i in R}.items() if v == max([i for i in {int(i): R.count(i) for i in R}.values()])]))
    R = int(R, 9)
    R = hex(R)[2:]
    if N < 10_000:
        if 'bac' in R:
            ans.append(N)
print(max(ans))
