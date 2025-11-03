from turtle import *

screensize(4000, 4000)
m = 30
tracer(False)

for i in range(3):
    fd(27 * m)
    rt(90)
    fd(12 * m)
    rt(90)

up()

fd(4 * m)
rt(90)
fd(6 * m)
lt(90)

down()

for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(4, 'red')

print(28 * 13 + 84 * 78 - 7 * 24)

update()
done()
