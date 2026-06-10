with open('../files/26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    max_row_seats = [M] * K
    for i in file:
        row, seat = map(int, i.split())
        max_row_seats[seat - 1] = min(max_row_seats[seat - 1], row - 1)
ans1 = max(min(max_row_seats[i], max_row_seats[i + 1]) for i in range(len(max_row_seats) - 1))
ans2 = K - max_row_seats[::-1].index(ans1) - 1

print(ans1, ans2)
