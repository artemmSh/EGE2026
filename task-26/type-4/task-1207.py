with open('../files/26_1207.txt') as file:
    S, N = map(int, file.readline().split())
    users = [int(i) for i in file]

S_tmp = S
users.sort()
archive = list()
for user in users:
    if S_tmp > user:
        archive.append(user)
        S_tmp -= user

archive = archive[:-1]

for user in users[::-1]:
    if S >= sum(archive) + user:
        archive.append(user)
        break
print(len(archive), archive[-1])
