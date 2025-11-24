def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]

for x in range(1, 2006)[::-1]:
    num = 43**56 + 113**841 - x
    con = converter(num, 4)
    if con.count('2') <= 712:
        con.replace('0', '*').replace('2', '*').replace('1', '+').replace('3', '+')
        if  not con.count('*') % 2 and not con.count('+') % 2:
            print(x)
            break