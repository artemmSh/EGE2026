with open('files/26_5066.txt') as file:
    N = int(file.readline())
    cases = [int(i) for i in file]

cases = sorted(cases, reverse=True)
cells = []

while cases:
    cells.append([cases[0]])
    cases = cases[1:]
    for case in cases:
        if cells[-1][-1] - case >= 7:
            cells[-1].append(case)
            cases.remove(case)

print(len(cells), len(cells[0]))
