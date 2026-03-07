with open('files/26_16335.txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file]

cakes.sort(reverse=True)

current_cake = cakes[0]
cnt = 1

for cake in cakes:
    if current_cake - cake >= 4:
        current_cake = cake
        cnt += 1
print(cnt, current_cake)
