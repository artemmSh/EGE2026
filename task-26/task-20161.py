with open('files/26_20161.txt') as file:
    N = int(file.readline())
    discount_1, discount_2 = list(), list()
    for i in file:
        cost, category = map(int, i.split())
        if category % 2 == 0:
            discount_1.append(cost)
        else:
            discount_2.append(cost)

discount_1.sort()
discount_2.sort(reverse=True)

with_discount_1 = sum(i * 7 // 10 for i in discount_1[:int(len(discount_1) * 0.7)]) + sum(
    i * 8 // 10 for i in discount_1[int(len(discount_1) * 0.7):])
with_discount_2 = sum(i * 85 // 100 for i in discount_2[:int(len(discount_2) * 0.25)]) + sum(
    discount_2[int(len(discount_2) * 0.25):])
ans_1 = with_discount_1 + with_discount_2
ans_2 = abs((sum(discount_1) - with_discount_1) - (sum(discount_2) - with_discount_2))
print(ans_1, ans_2)
