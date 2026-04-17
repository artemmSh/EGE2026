with open('files/26_27636.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

data.sort()

mks = []
for cont in data:
    if cont <= S:
        mks.append(cont)
        S -= cont
print(N - len(mks), sum(data) - sum(mks))
