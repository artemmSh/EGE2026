from turtle import *

screensize(4000, 4000)
m = 30
tracer(False)

for i in range(5):
    fd(37 * m)
    rt(90)
    fd(44 * m)
    rt(90)

up()

bk(18 * m)
rt(90)
fd(29 * m)
lt(90)

down()

for i in range(5):
    fd(31 * m)
    rt(90)
    fd(35 * m)
    rt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(4, 'red')

print(16 * 14)

update()
done()
