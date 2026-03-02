with open('files/24_14512.txt') as file:
    data = file.readline()

ans = 0
for l in range(len(data)):
    if data[l].isdigit():
        for r in range(l + 1, len(data)):
            if data[r].isdigit():
                if data[l] != data[r]:
                    if data[l + 1:r].isalpha():
                        if data[l + 1:r].count('B') == data[l + 1:r].count('C'):
                            ans = max(ans, len(data[l:r + 1]))
                break

print(ans)
