from timeit import timeit
def input_data():
    file = open('26_2944.txt')
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]
    file.close()
    return sorted(data), S, N





def solution():
    data, S, N = input_data()
    users = list()

    for i in data:
        if i <= S:
            S -= i
            users.append(i)
    removed_size = data[len(users) - 1]
    S += removed_size
    #print(len(users))
    for i in range(len(users), N):
        if removed_size < data[i] <= S:
            users.append(data[i])
    #print(users[-1])


print(timeit('solution()', globals=globals(), number=1000))