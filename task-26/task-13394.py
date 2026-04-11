from math import *

with open('files/26.6_13394.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]
    on_sale = [i for i in prices if i > 350]
    off_sale = [i for i in prices if i not in on_sale]

on_sale.sort(reverse=True)

quarter_prices = on_sale[2::3]
tmp = quarter_prices.copy()
default_prices = []
for x in on_sale:
    if x in tmp:
        tmp.remove(x)
    else:
        default_prices.append(x)

ans1 = sum(off_sale) + sum(default_prices) + sum(ceil(i / 4) for i in quarter_prices)
ans2 = ceil(sum(off_sale) + sum(on_sale[:-(len(on_sale) // 3)]) + sum(on_sale[-(len(on_sale) // 3):]) / 4)
print(ans1, ans2)
