with open('files/24_3792.txt') as file:
    data = file.readline()

ans = 0
for l in range(len(data)):
    if data[l] in 'ABC':
        for r in range(l + 1, len(data)):
            if data[r] in 'ABC':
                ans = max(ans, len(data[l:r + 1]))
            else:
                break
print(ans)
