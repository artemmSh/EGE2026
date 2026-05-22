with open('files/26_29234.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    requests = [list(map(int, i.split())) for i in file]

requests.sort()
pcs = [[[0, 0]] for i in range(K)]
for start, end in requests:
    for pc in range(len(pcs)):
        if start > pcs[pc][-1][-1]:
            pcs[pc].append([start, end])
            break
pcs = [pc[1:] for pc in pcs]
ans_1 = sum(len(pc) for pc in pcs)
ans_2 = max(sum((t[1] - t[0]) * ((t[1] - t[0]) + 1) // 2 for t in pc) for pc in pcs)
print(ans_1, ans_2)
