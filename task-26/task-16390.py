with open('files/26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    packages = [int(i) for i in file]

packages.sort()
max_packages_count = 0
S_tmp = S
for package in packages:
    if S_tmp >= package:
        max_packages_count += 1
        S_tmp -= package

print(max_packages_count, end=' ')

for max_package in sorted(packages, reverse=True):
    ans = []
    S_tmp = S
    if S_tmp >= max_package:
        ans.append(max_package)
        S_tmp -= max_package
    for package in packages:
        if S_tmp >= package:
            ans.append(package)
            S_tmp -= package
        if len(ans) == max_packages_count:
            print(max_package)
            exit()
