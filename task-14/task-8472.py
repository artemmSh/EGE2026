from string import printable as alph


def converter(x, base):
    res = ''
    while x:
        res += alph[x % base]
        x //= base
    return res[::-1]


for x in range(1, 100)[::-1]:
    num1 = 7*100**6+int('a', 36)*100**5+x*100**4+0*100**3+1*100**2+2*100**1+3*100**0
    num2 = 1*100**5+int('b', 36)*100**4+int('a', 36)*100**3+6*100**2+4*100**1+x*100**0
    num3 = x*100**6+9*100**5+8*100**4+0*100**3+1*100**2+2*100**1+int('c', 36)*100**0
    num = num1-num2+num3
    if not (num % 21):
        print(converter(x, 6))
        break
