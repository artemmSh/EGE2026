with open('26_4956.txt') as file:
    N, M = map(int, file.readline().split())
    cheap = dict()
    exp = dict()
    for i in file:
       price, status = map(int, i.split())
       if price <= M:
           if price in cheap:
               cheap[price][status] += 1
           else:
               cheap[price] = [0, 0]
               cheap[price][status] += 1
       else:
           if price in exp:
               exp[price][status] += 1
           else:
               exp[price] = [0, 0]
               exp[price][status] += 1
popular_cheap = min(cheap)
for product in cheap:
    if cheap[popular_cheap][1] < cheap[product][1]:
        popular_cheap = product
popular_exp = min(exp)
for prod in exp:
    if exp[popular_exp][1] < exp[prod][1]:
        popular_exp = prod
print(popular_cheap*cheap[popular_cheap][1]+popular_exp*exp[popular_exp][1], exp[popular_exp][0] + cheap[popular_cheap][0])
