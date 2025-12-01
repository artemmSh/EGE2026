num = 15*343**2031 + 7*49**1142 -3*7**111 + 7**222 - 16809

cnt_even = 0
cnt_odd = 0

while num:
    if (num % 7) % 2 == 0:
        cnt_even += 1
    else:
        cnt_odd += 1
    num //= 7
print(abs(cnt_odd-cnt_even))