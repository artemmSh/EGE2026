with open('files/26_18541.txt') as file:
    N, M = map(int, file.readline().split())
    data = [int(i) for i in file]
    kettlebells = data[:N]
    prs = data[-M:]

prs.sort(reverse=True)
kettlebells.sort(reverse=True)

used_weights = list()
for pr in prs:
    for kettlebell in kettlebells:
        if pr >= kettlebell:
            used_weights.append(kettlebell)
            break

ans1 = sum(used_weights) // len(used_weights)
ans2 = max(used_weights, key=lambda x: (used_weights.count(x)))

print(ans1, ans2)
