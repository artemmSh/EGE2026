with open('files/test.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]
