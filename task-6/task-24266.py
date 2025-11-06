from turtle import *

screensize(4000, 4000)
m = 15
tracer(False)

for i in range(4):
    fd(30 * m)  # я решил типо подбором просто типо короче там p = 18*2 + _*2 = 42 и получается 6 типо и я просто двигал короче туда сюда и короче со 2 попытки получилось
    rt(90)
    fd(48 * m)
    rt(90)

up()

fd(27 * m)
rt(90)
fd(24 * m)
lt(90)

down()

for i in range(4):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(10, 'white')

print(30)

update()
done()
