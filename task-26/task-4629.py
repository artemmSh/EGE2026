with open('files/26_4629.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices.sort()
sale_customer = prices[-(N // 4):]
sale_seller = prices[:N // 4]
customer_ans, seller_ans = sum(prices) - sum(sale_customer) // 2, sum(prices) - sum(sale_seller) // 2
print(customer_ans, seller_ans)
