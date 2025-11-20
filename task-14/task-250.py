ans = []
for N in range(1, 41):
    if bin(N)[-4:] == '1011':
        ans.append(N)
print(max(ans))
