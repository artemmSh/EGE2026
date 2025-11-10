from turtle import *

screensize(4000, 4000)
m = 15
tracer(False)

for i in range(9):
    fd(30 * m)
    rt(90)
    fd(12 * m)
    rt(90)

up()

lt(270)
fd(5 * m)
lt(90)

down()

for i in range(2):
    fd(24 * m)
    rt(90)
    fd(28 * m)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(10, 'white')

print((24 ** 2 + 7 ** 2) ** 0.5)

update()
done()
