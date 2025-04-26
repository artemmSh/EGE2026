from timeit import timeit

with open('26_21719.txt') as file:
    N = int(file.readline())
    tasks = [list(map(int, i.split())) for i in file]
def f():
    tasks.sort()

    counter = 1
    maximum = 0
    student_id = 0
    id_and_counter = []

    for i in range(N-1):
        previous, current = tasks[i][1], tasks[i+1][1]
        if tasks[i][0] == tasks[i+1][0]:
            if tasks[i][1] != tasks[i + 1][1]:
                if current-2 == previous:
                    counter+=1
                else:
                    counter = 1
        else:
            counter = 1
        id_and_counter.append([tasks[i][0], counter])
    id_and_counter.sort(key=lambda x: (x[1], -x[0]))
    #print(*id_and_counter[-1])
print(timeit(f, number=1000000))