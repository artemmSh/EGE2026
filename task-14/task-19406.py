from string import printable as alph

res = []
for x in alph[1:35][::-1]:
    num = int(f'6{x}qr{x}', 35) + int(f'{x}59sh', 35) + int(f'ph{x}69yw', 35)
    num = str(num)
    ans = 0
    for i in num:
        ans = max(num.count(i), ans)
    kaka = []
    for i in num:
        if num.count(i) == ans:
            kaka.append(i)
    ans = max(kaka)
    if int(num) % int(ans) ** 2 == 0:
        print(int(num) // int(ans) ** 2)
        break
