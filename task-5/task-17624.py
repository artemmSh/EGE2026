ans = []
for N in range(1, 1000000):
    R = bin(N)[2:]
    for i in range(2):
        R += str((sum(map(int, R))) % 2)
    R = int(R, 2)
    if R > 75:
        ans.append(R)
print(min(ans))