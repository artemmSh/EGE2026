ans = 0
for n in range(1, 100_000):
    r = bin(n)[2:]
    if sum(map(int, r)) % 2 == 0:
        r = '10' + r[2:] + '1'
    else:
        r = '11' + r[2:] + '0'
    r = int(r, 2)
    if n < 16:
        ans = max(ans, r)
print(ans)
