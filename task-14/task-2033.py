from string import printable as alph
num = 6*144**26 + 11*12**75 - 48
count = 0
while num:
    if alph[num % 12] == 'b':
        count += 1
    num //= 12
print(count)
