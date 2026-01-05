from turtle import *

screensize(4000, 4000)
m = 30
tracer(False)

for i in range(2):
    fd(14 * m)
    lt(270)
    bk(12 * m)
    rt(90)

up()
fd(9 * m)
rt(90)
bk(7 * m)
lt(90)
down()

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()

for x in range(-20, 40):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(4, 'red')

print(15 * 13 + 14 * 7 - 7 * 6)
update()
done()
