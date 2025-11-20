from string import printable as alph

N = 283 ** 382 + 9 ** 15 + 2 ** 3

cnt_B = 0
cnt_C = 0
while N:
    if alph[N % 14] == 'b':
        cnt_B += 1
    if alph[N % 14] == 'c':
        cnt_C += 1
    N //= 14
print(abs(cnt_C - cnt_B))
