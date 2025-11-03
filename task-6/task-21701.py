from turtle import *

screensize(4000, 4000)
m = 15
tracer(False)

for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)

up()

fd(14 * m)
rt(90)
fd(10 * m)
lt(90)

down()

for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(4, 'red')

print(29 * 19 + 31 * 8 - 8 * 15)

update()
done()
