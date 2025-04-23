with open('26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    results = list()
    for i in file:
        results.append(list(map(int, i.split())))

results.sort(key=lambda x: (x[1] + x[2] + x[3] + x[4], x[4], -x[0]), reverse=True)

candidate_id = 0
quantity = 0
half = 0
prohod = 0
for i in range(N):
    if results[K] == results[i]:
        half = results[K]
        quantity+=1
        prohod = results[K-1]
        candidate_id = prohod[0]
print(candidate_id, quantity)