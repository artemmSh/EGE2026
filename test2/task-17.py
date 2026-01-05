file = open('17 (1).txt')
data = [int(i) for i in file]
div_41_and_pol = [i for i in data if i != 0 and abs(i) == i and i % 41 == 0]

ans = []
for i in range(len(data) - 1):
    fir = data[i]
    sec = data[i + 1]
    if fir != sec and abs(fir - sec) % min(div_41_and_pol) == 0:
        ans.append(fir + sec)
print(len(ans), max(ans))
