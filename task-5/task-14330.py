for N in range(1_0000, 1_00000):
    summa = (int(max(set(str(N)))) + int(min(set(str(N))))) ** 2
    temp = [int(i) for i in str(N) if int(i) % 2 == 0]
    prod = 1
    for i in temp:
        prod *= i
    ans = sorted([summa, prod])
    ans = [str(i) for i in ans]
    ans = ''.join(ans)
    ans = int(ans)

    if ans == 12116:
        print(N)
        break
