with open('26_19256.txt') as file:
    N = int(file.readline())
    students = dict()
    for i in file:
        ident, num = map(int, i.split())
        if ident in students:
            students[ident].add(num)
        else:
            students[ident] = {num}

ans = []

for ident in students:
    student = sorted(students[ident])
    cnt = 1
    maximum = 0
    for i in range(len(student) - 1):
        previous, current = student[i], student[i + 1]
        if current - previous == 1:
            cnt += 1
        else:
            cnt = 1
        maximum = max(maximum, cnt)
    ans.append(([maximum, ident]))

ans.sort(key=lambda x: (-x[0],x[1]))
print(*ans[0][::-1])
