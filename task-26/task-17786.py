with open('files/26_17786.txt') as file:
    N, V = map(int, file.readline().split())
    watermelons = [int(i) / 1000 for i in file]

watermelons.sort(reverse=True)
ans = []
for watermelon in watermelons:
    if 7 <= watermelon <= 12 and V >= watermelon:
        ans.append(watermelon)
        V -= watermelon
print(len(ans), int(ans[-1] * 1000))
