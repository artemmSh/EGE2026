from filecmp import clear_cache


def s1(line):
    amount = [line.count(i) for i in set(line)]
    return sorted(amount) == [1, 1, 1, 1, 3]


def s2(line):
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    return sum(ne_pov) / len(ne_pov) <= pov[0]


with open('files/task-9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    if s1(line) and s2(line):
        cnt += 1
print(cnt)
