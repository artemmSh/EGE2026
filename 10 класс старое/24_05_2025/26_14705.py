from timeit import timeit


def input_data() -> tuple[int, list[list[int]]]:
    with open('26_14705.txt') as file:
        return int(file.readline()), [list(map(int, i.split())) for i in file]


def solution_1(data: list[list[int]]) -> tuple[int, list[int]]:
    timeline = [0] * 5_000_010
    for i in data:
        timeline[i[0]] += 1
        timeline[i[1]] -= 1

    maximum = 0
    cnt = 0
    for i in timeline:
        cnt += i
        maximum = max(maximum,cnt)

    return maximum, timeline


def solution_2(time_line: list[int]) -> int:
    counter = 0
    cnt = 0
    ans2 = 0
    for i in timeline:
        cnt += i
        if cnt == maximum:
            counter += 1
        else:
            counter = 0
        ans2 = max(ans2, counter)
    return ans2


N, data = input_data()
maximum, timeline = solution_1(data)
print(maximum, solution_2(timeline))

time1 = timeit('input_data()', globals=globals(), number=10)
time2 = timeit('solution_1(data)', globals=globals(), number=10)
time3 = timeit('solution_2(timeline)', globals=globals(), number=10)
print(time1, time2, time3)