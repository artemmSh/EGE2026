def read_file(file_name):
    with open(file_name) as file:
        N = int(file.readline())
        data = []
        for i in file:
            data.append(list(map(int, i.split())))
        return N, data

def solution():
    N, data = read_file('26_21598.txt')
    time = [0] * 1441
    for i in data:
        for j in range(i[0], i[1]+1):
            time[j] +=1
    changes_count_workers = []
    for i in range(len(time)-1):
        if time[i] != time[i+1]:
            changes_count_workers.append(i)
    print(changes_count_workers[-2])
solution()